#!/usr/bin/env python3
import ctypes
import ctypes.util
import os
import re
import select
import sys
import time
from pathlib import Path

ROOT = Path(os.environ.get("SIGMA_ROOT", str(Path.home() / "SIGMA" / "sigma_genesis1")))
STATE = Path(os.environ.get("C5_STATE_ROOT", str(ROOT / ".sigma_c5_real_shadow_v2")))
EXEC = STATE / "runtime" / ".sigma_exec" / "SIGMA_C5_AUTONOMOUS_SELF_LEARNING"
ST = EXEC / "state"
IO = EXEC / "io"

LOCAL = ST / "local_active_record.txt"
EXTERNAL = ST / "external_active_record.txt"
CURRENT = IO / "current_stream.txt"
SEGMENT_ID = IO / "segment_entry_id.txt"

OPS = ROOT / ".sigma_ops"
STATUS = OPS / "SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.status"
LOG = ROOT / "SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.log"
PIDFILE = OPS / "SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.pid"

ENTRY_RE = re.compile(r"ENTRY_ID\s*=\s*([^| \r\n]+)")
last_status = None


def read_bytes(path: Path):
    try:
        return path.read_bytes()
    except FileNotFoundError:
        return None
    except OSError:
        return None


def read_text_value(path: Path) -> str:
    raw = read_bytes(path)
    if raw is None:
        return ""
    return raw.decode("utf-8", "replace").strip()


def marker(path: Path):
    raw = read_bytes(path)
    if raw is None:
        return ("ABSENT", "")
    text = raw.decode("utf-8", "replace")
    if not text.strip():
        return ("EMPTY", "")
    m = ENTRY_RE.search(text)
    if not m:
        return ("UNKNOWN", "")
    return ("VALID", m.group(1))


def atomic_write(path: Path, value: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    desired = value.rstrip("\n") + "\n"
    try:
        if path.read_text(encoding="utf-8", errors="replace") == desired:
            return False
    except (FileNotFoundError, OSError):
        pass
    tmp = path.with_name(path.name + f".partial.{os.getpid()}")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(desired)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    return True


def emit_status(lines):
    global last_status
    text = "\n".join(lines) + "\n"
    OPS.mkdir(parents=True, exist_ok=True)
    atomic_write(STATUS, text)
    if text != last_status:
        stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(stamp + " " + " ".join(lines) + "\n")
        last_status = text


def reconcile():
    lclass, lid = marker(LOCAL)
    eclass, eid = marker(EXTERNAL)
    seg = read_text_value(SEGMENT_ID)
    cur = read_text_value(CURRENT).upper()

    matches = []
    if seg and lclass == "VALID" and seg == lid:
        matches.append("LOCAL")
    if seg and eclass == "VALID" and seg == eid:
        matches.append("EXTERNAL")

    desired = ""
    reason = ""

    if len(matches) == 1:
        desired = matches[0]
        reason = "SEGMENT_ENTRY_MATCH"
    elif len(matches) > 1:
        reason = "AMBIGUOUS_SEGMENT_ENTRY_MATCH"
    elif lclass == "VALID" and eclass != "VALID":
        desired = "LOCAL"
        reason = "ONLY_VALID_ACTIVE_RECORD"
    elif eclass == "VALID" and lclass != "VALID":
        desired = "EXTERNAL"
        reason = "ONLY_VALID_ACTIVE_RECORD"
    elif lclass == "VALID" and eclass == "VALID":
        if cur == "LOCAL":
            desired = "LOCAL"
            reason = "PRESERVE_VALID_CURRENT_STREAM"
        elif cur == "EXTERNAL":
            desired = "EXTERNAL"
            reason = "PRESERVE_VALID_CURRENT_STREAM"
        else:
            reason = "DUAL_VALID_ACTIVE_NO_SEGMENT_MATCH"
    else:
        reason = "NO_VALID_ACTIVE_RECORD"

    changed = False
    if desired:
        changed = atomic_write(CURRENT, desired)

    lines = [
        "STREAM_COHERENCE_WATCHER=ACTIVE",
        f"LOCAL_MARKER_CLASS={lclass}",
        f"LOCAL_ENTRY_ID={lid or 'NONE'}",
        f"EXTERNAL_MARKER_CLASS={eclass}",
        f"EXTERNAL_ENTRY_ID={eid or 'NONE'}",
        f"SEGMENT_ENTRY_ID={seg or 'NONE'}",
        f"CURRENT_STREAM_OBSERVED={cur or 'NONE'}",
        f"CURRENT_STREAM_DESIRED={desired or 'HOLD'}",
        f"COHERENCE_REASON={reason}",
        f"CURRENT_STREAM_REWRITTEN={'YES' if changed else 'NO'}",
        "HOST_SEMANTIC_SELECTION=NO",
    ]
    emit_status(lines)


IN_MODIFY = 0x00000002
IN_ATTRIB = 0x00000004
IN_CLOSE_WRITE = 0x00000008
IN_MOVED_FROM = 0x00000040
IN_MOVED_TO = 0x00000080
IN_CREATE = 0x00000100
IN_DELETE = 0x00000200
IN_DELETE_SELF = 0x00000400
IN_MOVE_SELF = 0x00000800
MASK = (
    IN_MODIFY
    | IN_ATTRIB
    | IN_CLOSE_WRITE
    | IN_MOVED_FROM
    | IN_MOVED_TO
    | IN_CREATE
    | IN_DELETE
    | IN_DELETE_SELF
    | IN_MOVE_SELF
)


def open_inotify():
    libc_name = ctypes.util.find_library("c")
    if not libc_name:
        return None
    libc = ctypes.CDLL(libc_name, use_errno=True)
    init = libc.inotify_init1
    init.argtypes = [ctypes.c_int]
    init.restype = ctypes.c_int
    add = libc.inotify_add_watch
    add.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_uint32]
    add.restype = ctypes.c_int

    flags = getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_CLOEXEC", 0)
    fd = init(flags)
    if fd < 0:
        return None

    for directory in (ST, IO):
        directory.mkdir(parents=True, exist_ok=True)
        wd = add(fd, os.fsencode(str(directory)), MASK)
        if wd < 0:
            os.close(fd)
            return None
    return fd


def main():
    OPS.mkdir(parents=True, exist_ok=True)
    PIDFILE.write_text(str(os.getpid()) + "\n", encoding="utf-8")
    reconcile()

    fd = open_inotify()
    try:
        while True:
            if fd is None:
                time.sleep(0.02)
                reconcile()
                continue

            ready, _, _ = select.select([fd], [], [], 0.10)
            if ready:
                try:
                    os.read(fd, 65536)
                except BlockingIOError:
                    pass
                except OSError:
                    try:
                        os.close(fd)
                    except OSError:
                        pass
                    fd = open_inotify()
            reconcile()
    except KeyboardInterrupt:
        return 0
    finally:
        try:
            PIDFILE.unlink()
        except FileNotFoundError:
            pass
        if fd is not None:
            try:
                os.close(fd)
            except OSError:
                pass


if __name__ == "__main__":
    sys.exit(main())
