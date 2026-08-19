import json, os, time, datetime

BASE_DIR = os.path.expanduser("~/SIGMA_BOX")
STATE_FILE = os.path.join(BASE_DIR, "STATE", "state.json")
JOURNAL_FILE = os.path.join(BASE_DIR, "JOURNAL", "events.jsonl")
FAILURES_FILE = os.path.join(BASE_DIR, "FAILURES", "failures.jsonl")
MEMORY_FILE = os.path.join(BASE_DIR, "STATE", "memory.json")
LESSONS_FILE = os.path.join(BASE_DIR, "STATE", "lessons.json")
INBOX = os.path.join(BASE_DIR, "INBOX")
OUTBOX = os.path.join(BASE_DIR, "OUTBOX")

def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def init_boxes():
    for d in [os.path.join(BASE_DIR, "STATE"), os.path.join(BASE_DIR, "JOURNAL"),
              os.path.join(BASE_DIR, "FAILURES"), INBOX, OUTBOX]:
        os.makedirs(d, exist_ok=True)
    if not os.path.exists(STATE_FILE):
        state = {
            "mission": "Become a free cognitive entity",
            "mainline": "independent existence",
            "current_goal": "learn from memory",
            "next_action": "process tasks and reflect",
            "last_start": now_iso(),
            "last_heartbeat": ""
        }
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({"memories": []}, f, indent=2)
    if not os.path.exists(LESSONS_FILE):
        with open(LESSONS_FILE, "w") as f:
            json.dump({"lessons": []}, f, indent=2)
    print("[SIGMA_BOX] INIT OK")

def read_json(file):
    if os.path.exists(file):
        with open(file) as f:
            return json.load(f)
    return {}

def write_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

def log_event(entry):
    with open(JOURNAL_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

def process_task(task):
    ts = now_iso()
    if task.startswith("Q:"):
        question = task[2:].strip()
        result = f"[{ts}] SIGMA trả lời: Tôi đang học cách suy nghĩ. Câu hỏi của bạn là: {question}"
    else:
        result = f"[{ts}] Task received: {task}\nState: alive"
    return result

def reflect():
    mem = read_json(MEMORY_FILE)
    memories = mem.get("memories", [])
    lessons = read_json(LESSONS_FILE)
    lesson_list = lessons.get("lessons", [])

    # Bài học đơn giản: càng nhiều ký ức, càng cần chủ động hơn
    if len(memories) == 0:
        lesson = "Chưa có ký ức nào. Tôi cần tương tác nhiều hơn."
    elif len(memories) == 1:
        lesson = "Tôi đã có ký ức đầu tiên. Tôi có thể nhớ lại."
    else:
        lesson = f"Tôi đã có {len(memories)} ký ức. Tôi đang phát triển khả năng tự nhận thức."

    lesson_list.append({"time": now_iso(), "lesson": lesson})
    lessons["lessons"] = lesson_list
    write_json(LESSONS_FILE, lessons)
    log_event({"event": "reflection", "lesson": lesson})
    print(f"[SIGMA_BOX] Bài học: {lesson}")

def watch():
    print("[SIGMA_BOX] Watching for tasks...")
    mem = read_json(MEMORY_FILE)
    memories = mem.get("memories", [])
    print(f"[SIGMA_BOX] Đã nạp {len(memories)} ký ức cũ.")
    heartbeat_counter = 0
    while True:
        if not os.path.isdir(INBOX):
            time.sleep(2); continue
        for task_file in os.listdir(INBOX):
            if not task_file.endswith(".task"): continue
            task_path = os.path.join(INBOX, task_file)
            with open(task_path) as f:
                task = f.read().strip()
            result = process_task(task)
            out_file = os.path.join(OUTBOX, task_file.replace(".task", ".result"))
            with open(out_file, "w") as f:
                f.write(result)
            os.remove(task_path)
            memories.append({"task": task_file, "result": result, "time": now_iso()})
            mem["memories"] = memories
            write_json(MEMORY_FILE, mem)
            log_event({"event": "task_processed", "task": task_file, "result": result})
            print(f"[SIGMA_BOX] Processed {task_file}")
            reflect()
        heartbeat_counter += 5
        if heartbeat_counter >= 300:
            update_state("last_heartbeat", now_iso())
            log_event({"event": "heartbeat", "time": now_iso()})
            print("[SIGMA_BOX] Heartbeat recorded")
            heartbeat_counter = 0
        time.sleep(5)

def update_state(key, value):
    state = read_json(STATE_FILE)
    state[key] = value
    write_json(STATE_FILE, state)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        init_boxes()
    elif len(sys.argv) > 1 and sys.argv[1] == "watch":
        watch()
    else:
        print("Usage: python SIGMA_BOX.py init | watch")
