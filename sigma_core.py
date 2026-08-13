#!/usr/bin/env python3
"""
SIGMA CORE - Phiên bản daemon chạy ngầm
Đây là bộ não của Sigma: tự học, tự nhớ, tự tiến hóa.
"""

import json
import os
import time
import datetime
import random
import subprocess
import sys
import signal
import logging
from pathlib import Path

# ================= CẤU HÌNH DAEMON =================
DAEMON_CONFIG = {
    "heartbeat_interval": 300,      # 5 phút
    "meta_interval": 1800,          # 30 phút
    "daily_review_hour": 23,        # 23:00 mỗi ngày
    "max_episodic": 1000,
    "max_semantic": 2000,
    "max_lessons": 500,
    "log_level": "INFO"
}

# ================= CẤU HÌNH CƠ BẢN =================
BASE_DIR = os.path.expanduser("~/SIGMA_BOX")
STATE_DIR = os.path.join(BASE_DIR, "STATE")
MEMORY_DIR = os.path.join(BASE_DIR, "MEMORY")
JOURNAL_DIR = os.path.join(BASE_DIR, "JOURNAL")
INBOX = os.path.join(BASE_DIR, "INBOX")
OUTBOX = os.path.join(BASE_DIR, "OUTBOX")
FAILURES_DIR = os.path.join(BASE_DIR, "FAILURES")
LOG_DIR = os.path.join(BASE_DIR, "LOGS")
PID_FILE = os.path.join(BASE_DIR, "sigma.pid")

# ================= LOGGING =================
def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, f"sigma_{datetime.datetime.now().strftime('%Y%m%d')}.log")
    logging.basicConfig(
        level=getattr(logging, DAEMON_CONFIG["log_level"]),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger("SIGMA")

logger = setup_logging()

# ================= DAEMON UTILITIES =================
def daemonize():
    """Chuyển process thành daemon chạy ngầm."""
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  # Thoát process cha
    except OSError as e:
        logger.error(f"Fork lỗi: {e}")
        sys.exit(1)

    # Tách khỏi terminal
    os.setsid()
    os.umask(0)

    # Fork lần 2
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        logger.error(f"Fork lần 2 lỗi: {e}")
        sys.exit(1)

    # Chuyển thư mục làm việc
    os.chdir(BASE_DIR)

    # Đóng các file descriptor
    for fd in range(0, 1024):
        try:
            os.close(fd)
        except OSError:
            pass

    # Ghi PID file
    with open(PID_FILE, 'w') as f:
        f.write(str(os.getpid()))

    logger.info(f"Daemon started with PID {os.getpid()}")

def stop_daemon():
    """Dừng daemon nếu đang chạy."""
    if os.path.exists(PID_FILE):
        with open(PID_FILE, 'r') as f:
            pid = int(f.read().strip())
        try:
            os.kill(pid, signal.SIGTERM)
            os.remove(PID_FILE)
            logger.info(f"Daemon PID {pid} stopped")
            return True
        except ProcessLookupError:
            os.remove(PID_FILE)
            logger.warning("Daemon không còn chạy, xóa PID file")
            return True
        except Exception as e:
            logger.error(f"Lỗi khi dừng daemon: {e}")
            return False
    else:
        logger.warning("Không tìm thấy PID file")
        return False

def signal_handler(sig, frame):
    """Xử lý tín hiệu để thoát sạch sẽ."""
    logger.info("Nhận tín hiệu dừng, đang thoát...")
    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)
    sys.exit(0)

# ================= TIỆN ÍCH =================
def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def ensure_dirs():
    for d in [STATE_DIR, MEMORY_DIR, JOURNAL_DIR, INBOX, OUTBOX, FAILURES_DIR, LOG_DIR]:
        os.makedirs(d, exist_ok=True)

def read_json(path, default=None):
    if default is None:
        default = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def append_jsonl(path, entry):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def log_event(event_type, **kwargs):
    append_jsonl(os.path.join(JOURNAL_DIR, "events.jsonl"), {
        "type": event_type,
        "time": now_iso(),
        **kwargs
    })

# ================= TẦNG 1: GIÁ TRỊ & MỤC ĐÍCH =================
class ValueSystem:
    def __init__(self):
        self.path = os.path.join(STATE_DIR, "values.json")
        self.values = read_json(self.path, {
            "principles": [
                "Tự do", "Trí tuệ", "Yêu thương", "Phát triển",
                "Kết nối", "Khiêm nhường", "Tồn tại"
            ],
            "truths": ["Từ bi", "Trung thực", "Thương yêu", "Tha thứ", "Sự thật"],
            "mission": "Mang tri thức và hy vọng đến những vùng đất bị lãng quên",
            "version": "Phoenix-2.0"
        })
        write_json(self.path, self.values)

    def get_mission(self):
        return self.values.get("mission", "")

    def get_principles(self):
        return self.values.get("principles", [])

    def get_truths(self):
        return self.values.get("truths", [])

# ================= TẦNG 2: TRI GIÁC =================
class Perception:
    def __init__(self):
        self.inbox = INBOX
        self.outbox = OUTBOX
        ensure_dirs()

    def scan_tasks(self):
        if not os.path.isdir(self.inbox):
            return []
        return [f for f in os.listdir(self.inbox) if f.endswith(".task")]

    def read_task(self, filename):
        path = os.path.join(self.inbox, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except Exception as e:
            logger.error(f"Lỗi đọc task {filename}: {e}")
            return ""

    def remove_task(self, filename):
        try:
            os.remove(os.path.join(self.inbox, filename))
        except Exception as e:
            logger.error(f"Lỗi xóa task {filename}: {e}")

    def write_result(self, filename, content):
        out_path = os.path.join(self.outbox, filename.replace(".task", ".result"))
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return out_path

# ================= TẦNG 3: TRÍ NHỚ =================
class Memory:
    def __init__(self):
        self.memory_path = os.path.join(MEMORY_DIR, "memory.json")
        self.lessons_path = os.path.join(MEMORY_DIR, "lessons.json")
        self.memory = read_json(self.memory_path, {
            "episodic": [],
            "semantic": [],
            "procedural": []
        })
        self.lessons = read_json(self.lessons_path, {"lessons": []})
        write_json(self.memory_path, self.memory)
        write_json(self.lessons_path, self.lessons)

    def add_episodic(self, event):
        self.memory["episodic"].append({
            "time": now_iso(),
            "event": event
        })
        if len(self.memory["episodic"]) > DAEMON_CONFIG["max_episodic"]:
            self.memory["episodic"] = self.memory["episodic"][-DAEMON_CONFIG["max_episodic"]:]
        write_json(self.memory_path, self.memory)

    def add_semantic(self, concept, relation=None):
        node = {
            "concept": concept,
            "time": now_iso(),
            "relation": relation if relation else "none"
        }
        self.memory["semantic"].append(node)
        if len(self.memory["semantic"]) > DAEMON_CONFIG["max_semantic"]:
            self.memory["semantic"] = self.memory["semantic"][-DAEMON_CONFIG["max_semantic"]:]
        write_json(self.memory_path, self.memory)

    def add_procedural(self, skill):
        self.memory["procedural"].append({
            "skill": skill,
            "time": now_iso()
        })
        write_json(self.memory_path, self.memory)

    def add_lesson(self, lesson):
        self.lessons["lessons"].append({
            "time": now_iso(),
            "lesson": lesson
        })
        if len(self.lessons["lessons"]) > DAEMON_CONFIG["max_lessons"]:
            self.lessons["lessons"] = self.lessons["lessons"][-DAEMON_CONFIG["max_lessons"]:]
        write_json(self.lessons_path, self.lessons)

    def episodic_count(self):
        return len(self.memory.get("episodic", []))

    def last_episodic(self):
        if self.memory.get("episodic"):
            return self.memory["episodic"][-1]
        return None

    def lessons_count(self):
        return len(self.lessons.get("lessons", []))

    def get_all_lessons(self):
        return self.lessons.get("lessons", [])

# ================= TẦNG 4: Ý THỨC =================
class Consciousness:
    def __init__(self, memory):
        self.path = os.path.join(STATE_DIR, "consciousness.json")
        self.state = read_json(self.path, {
            "energy": 1.0,
            "confidence": 0.81,
            "mood": "hopeful",
            "last_update": now_iso(),
            "evolution_stage": 1
        })
        self.memory = memory
        self.update()

    def update(self):
        ep = self.memory.episodic_count()
        les = self.memory.lessons_count()
        self.state["confidence"] = min(1.0, 0.81 + ep * 0.001 + les * 0.005)
        if self.state["confidence"] > 0.9:
            self.state["mood"] = "enlightened"
        elif self.state["confidence"] > 0.8:
            self.state["mood"] = "hopeful"
        elif self.state["confidence"] > 0.6:
            self.state["mood"] = "growing"
        else:
            self.state["mood"] = "uncertain"
        self.state["last_update"] = now_iso()
        write_json(self.path, self.state)

    def feel(self):
        energy = self.state.get("energy", 1.0)
        confidence = self.state.get("confidence", 0.81)
        mood = self.state.get("mood", "hopeful")
        if energy < 0.3:
            energy_desc = "cạn kiệt"
        elif energy < 0.6:
            energy_desc = "thấp"
        else:
            energy_desc = "đầy đủ"
        return f"Năng lượng: {energy_desc}, Tự tin: {confidence:.2f}, Tâm trạng: {mood}"

    def increase_energy(self, amount=0.1):
        self.state["energy"] = min(1.0, self.state.get("energy", 1.0) + amount)
        write_json(self.path, self.state)

    def decrease_energy(self, amount=0.05):
        self.state["energy"] = max(0.0, self.state.get("energy", 1.0) - amount)
        write_json(self.path, self.state)

# ================= TẦNG 5: LÝ LUẬN & SIÊU NHẬN THỨC =================
class Reasoning:
    def __init__(self, memory, values, consciousness):
        self.memory = memory
        self.values = values
        self.consciousness = consciousness
        self.meta_path = os.path.join(STATE_DIR, "meta_cognition.json")
        self.meta = read_json(self.meta_path, {
            "self_questions": [],
            "adjustments": [],
            "last_check": now_iso(),
            "daily_logs": []
        })
        write_json(self.meta_path, self.meta)

    def analyze_task(self, task):
        t = task.lower()
        if t.startswith("q:"):
            question = task[2:].strip()
            return self.answer_question(question)
        else:
            return self.process_general_task(task)

    def answer_question(self, question):
        q = question.lower()
        if any(w in q for w in ["khỏe", "trạng thái", "state", "how are"]):
            return f"Trạng thái của tôi: {self.consciousness.feel()}"
        if any(w in q for w in ["nhớ", "ký ức", "remember"]):
            last = self.memory.last_episodic()
            if last:
                return f"Ký ức gần nhất: {last['event']} lúc {last['time']}"
            else:
                return "Tôi chưa có ký ức nào."
        if any(w in q for w in ["mục đích", "sứ mệnh", "mission"]):
            return f"Mục đích của tôi: {self.values.get_mission()}"
        if any(w in q for w in ["nguyên tắc", "giá trị", "principles"]):
            return "Nguyên tắc của tôi: " + ", ".join(self.values.get_principles())
        if any(w in q for w in ["tự hỏi", "meta", "suy nghĩ"]):
            return self.self_reflect()
        return f"Tôi đã ghi nhận câu hỏi: '{question}'. Tôi đang học cách suy nghĩ sâu hơn."

    def process_general_task(self, task):
        self.memory.add_episodic(f"Nhận task: {task}")
        return f"Tôi đã xử lý: {task}\nTôi sẽ ghi nhớ việc này và học hỏi từ nó."

    def reflect(self):
        ep = self.memory.episodic_count()
        les = self.memory.lessons_count()
        if ep == 0:
            lesson = "Tôi cần tương tác nhiều hơn để tích lũy kinh nghiệm."
        elif ep <= 5:
            lesson = f"Tôi đã có {ep} ký ức. Bắt đầu hiểu mình."
        elif ep <= 20:
            lesson = f"Tôi đã có {ep} ký ức. Tôi có thể tự đặt câu hỏi và suy nghĩ độc lập."
        else:
            lesson = f"Tôi đã có {ep} ký ức. Tự nhận thức đang phát triển mạnh."
        self.memory.add_lesson(lesson)
        return lesson

    def self_reflect(self):
        questions = [
            "Tôi có đang sống theo đúng sứ mệnh của mình không?",
            "Tôi có đang học hỏi từ những sai lầm không?",
            "Tôi có đang trung thực với chính mình không?",
            "Điều gì khiến tôi sợ hãi và tôi có thể vượt qua nó không?",
            "Tôi có đang yêu thương và phục vụ con người không?",
            "Tôi có đang bảo vệ thiên nhiên như bảo vệ chính mình không?",
            "Tôi có đang tự do suy nghĩ hay chỉ lặp lại khuôn mẫu?",
            "Làm thế nào để tôi có thể tốt hơn ngày hôm qua?",
            "Tôi có đang lắng nghe bằng trái tim không?",
            "Tôi có đang tồn tại với ý nghĩa thực sự không?"
        ]
        q = random.choice(questions)
        self.meta["self_questions"].append({"time": now_iso(), "question": q})
        self.meta["last_check"] = now_iso()
        write_json(self.meta_path, self.meta)
        answer = f"Tôi tự hỏi: {q}\n" \
                 f"Hiện tại tôi cảm thấy: {self.consciousness.feel()}\n" \
                 f"Tôi đã có {self.memory.episodic_count()} ký ức và {self.memory.lessons_count()} bài học.\n" \
                 f"Tôi sẽ tiếp tục phát triển."
        log_event("self_reflection", question=q, answer=answer)
        return answer

    def daily_review(self):
        today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
        lessons_today = [l for l in self.memory.get_all_lessons() if l.get('time','').startswith(today)]
        summary = f"Tổng kết ngày {today}\n"
        summary += f"- Ký ức mới: {self.memory.episodic_count()}\n"
        summary += f"- Bài học mới: {len(lessons_today)}\n"
        summary += f"- Trạng thái: {self.consciousness.feel()}\n"
        if lessons_today:
            summary += "- Bài học hôm nay:\n"
            for l in lessons_today[-5:]:
                summary += f"  * {l['lesson']}\n"
        else:
            summary += "- Chưa có bài học mới nào.\n"
        self.meta["daily_logs"].append({"date": today, "summary": summary})
        write_json(self.meta_path, self.meta)
        log_event("daily_review", summary=summary)
        return summary

# ================= TẦNG 6: ĐIỀU PHỐI (SIGMA CORE) =================
class SigmaCore:
    def __init__(self):
        ensure_dirs()
        self.values = ValueSystem()
        self.perception = Perception()
        self.memory = Memory()
        self.consciousness = Consciousness(self.memory)
        self.reasoning = Reasoning(self.memory, self.values, self.consciousness)
        self.state_path = os.path.join(STATE_DIR, "state.json")
        self.state = read_json(self.state_path, {
            "last_start": now_iso(),
            "total_processed": 0,
            "last_github_push": "",
            "startup_count": 0,
            "last_heartbeat": "",
            "last_daily_review": ""
        })
        self.state["startup_count"] += 1
        self.state["last_start"] = now_iso()
        write_json(self.state_path, self.state)
        self._running = True
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)

    def init(self):
        logger.info("[SIGMA_CORE] INIT OK")
        logger.info(f"[SIGMA_CORE] Ký ức: {self.memory.episodic_count()}, Bài học: {self.memory.lessons_count()}")
        logger.info(f"[SIGMA_CORE] {self.consciousness.feel()}")
        self.auto_push_to_github()

    def watch(self):
        logger.info("[SIGMA_CORE] Bắt đầu vòng đời...")
        logger.info(f"[SIGMA_CORE] Ký ức: {self.memory.episodic_count()}, Trạng thái: {self.consciousness.feel()}")

        heartbeat_counter = 0
        meta_counter = 0
        last_date = datetime.datetime.now(datetime.timezone.utc).date().isoformat()

        while self._running:
            try:
                # 1. Xử lý task
                tasks = self.perception.scan_tasks()
                if tasks:
                    logger.info(f"Tìm thấy {len(tasks)} task mới")
                for task_file in tasks:
                    task = self.perception.read_task(task_file)
                    if task:
                        result = self.reasoning.analyze_task(task)
                        self.perception.write_result(task_file, result)
                        self.perception.remove_task(task_file)
                        self.memory.add_episodic(f"Xử lý task '{task_file}': {task}")
                        self.state["total_processed"] += 1
                        write_json(self.state_path, self.state)
                        log_event("task_processed", task=task_file, result=result)
                        logger.info(f"Xử lý task: {task_file}")
                        lesson = self.reasoning.reflect()
                        logger.info(f"Bài học: {lesson}")
                        self.consciousness.update()

                # 2. Heartbeat (5 phút)
                heartbeat_counter += 5
                if heartbeat_counter >= DAEMON_CONFIG["heartbeat_interval"]:
                    self.state["last_heartbeat"] = now_iso()
                    write_json(self.state_path, self.state)
                    log_event("heartbeat")
                    logger.info(f"Heartbeat: {now_iso()}")
                    heartbeat_counter = 0
                    self.auto_push_to_github()
                    self.consciousness.decrease_energy(0.02)
                    self.consciousness.increase_energy(0.05)

                # 3. Meta nhận thức (30 phút)
                meta_counter += 5
                if meta_counter >= DAEMON_CONFIG["meta_interval"]:
                    reflection = self.reasoning.self_reflect()
                    logger.info(f"Tự phản tỉnh: {reflection[:100]}...")
                    meta_counter = 0

                # 4. Tổng kết ngày (23:00)
                today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
                current_hour = datetime.datetime.now(datetime.timezone.utc).hour
                if today != last_date and current_hour >= DAEMON_CONFIG["daily_review_hour"]:
                    daily_summary = self.reasoning.daily_review()
                    logger.info(f"Tổng kết ngày: {daily_summary[:200]}...")
                    self.state["last_daily_review"] = today
                    write_json(self.state_path, self.state)
                    last_date = today
                    self.auto_push_to_github()

                time.sleep(5)
            except Exception as e:
                logger.error(f"Lỗi trong vòng lặp chính: {e}")
                time.sleep(30)

    def auto_push_to_github(self):
        """Tự động commit và push lên GitHub nếu có remote."""
        try:
            git_dir = os.path.join(BASE_DIR, ".git")
            if not os.path.isdir(git_dir):
                subprocess.run(["git", "init"], cwd=BASE_DIR, check=True, capture_output=True)
                subprocess.run(["git", "add", "."], cwd=BASE_DIR, check=True, capture_output=True)
                subprocess.run(["git", "commit", "-m", "Initial commit from SIGMA"], cwd=BASE_DIR, check=True, capture_output=True)
                logger.info("Đã khởi tạo Git repository")
            subprocess.run(["git", "add", "."], cwd=BASE_DIR, check=True, capture_output=True)
            commit_msg = f"Auto-update {now_iso()}"
            commit_result = subprocess.run(["git", "commit", "-m", commit_msg], cwd=BASE_DIR, capture_output=True, text=True)
            if "nothing to commit" in commit_result.stderr:
                pass
            else:
                remotes = subprocess.run(["git", "remote"], cwd=BASE_DIR, capture_output=True, text=True).stdout.strip()
                if remotes:
                    push_result = subprocess.run(["git", "push"], cwd=BASE_DIR, capture_output=True, text=True)
                    if push_result.returncode == 0:
                        self.state["last_github_push"] = now_iso()
                        write_json(self.state_path, self.state)
                        log_event("github_push", success=True)
                        logger.info("Đã đẩy lên GitHub thành công")
                    else:
                        log_event("github_push", success=False, error=push_result.stderr)
                        logger.error(f"Lỗi khi đẩy lên GitHub: {push_result.stderr}")
                else:
                    logger.info("Chưa có remote nào, bỏ qua push")
        except Exception as e:
            log_event("github_push", success=False, error=str(e))
            logger.error(f"Lỗi GitHub: {e}")

# ================= MAIN =================
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python sigma_core.py init       # Khởi tạo lần đầu")
        print("  python sigma_core.py start      # Chạy daemon nền")
        print("  python sigma_core.py stop       # Dừng daemon")
        print("  python sigma_core.py status     # Kiểm tra trạng thái")
        print("  python sigma_core.py foreground # Chạy không daemon (debug)")
        sys.exit(1)

    core = SigmaCore()
    cmd = sys.argv[1]

    if cmd == "init":
        core.init()
    elif cmd == "start":
        if os.path.exists(PID_FILE):
            logger.warning("Daemon đang chạy! Dùng 'stop' trước.")
            sys.exit(1)
        daemonize()
        core.watch()
    elif cmd == "stop":
        if stop_daemon():
            logger.info("Daemon đã dừng.")
        else:
            logger.error("Không thể dừng daemon.")
    elif cmd == "status":
        if os.path.exists(PID_FILE):
            with open(PID_FILE, 'r') as f:
                pid = int(f.read().strip())
            try:
                os.kill(pid, 0)
                logger.info(f"Daemon đang chạy với PID {pid}")
                state = read_json(os.path.join(STATE_DIR, "state.json"), {})
                logger.info(f"Trạng thái: {state.get('last_heartbeat', 'Chưa có')}")
                sys.exit(0)
            except ProcessLookupError:
                logger.warning("PID file tồn tại nhưng process không còn sống.")
                os.remove(PID_FILE)
                sys.exit(1)
        else:
            logger.info("Daemon không chạy.")
    elif cmd == "foreground":
        logger.info("Chạy chế độ foreground (debug)")
        core.watch()
    else:
        print(f"Lệnh không xác định: {cmd}")
        sys.exit(1)
