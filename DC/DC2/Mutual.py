import threading, time

lock = threading.Lock()
procs = {1: 0.5, 2: 0.3, 3: 0.7}  # process: CS time

def process(i, cs_time):
    print(f"P{i} → Requesting CS")
    lock.acquire()
    print(f"P{i} → Entered CS ✅ (holds for {cs_time}s)")
    time.sleep(cs_time)
    print(f"P{i} → Leaving CS 🚪")
    lock.release()

[threading.Thread(target=process, args=(i, t)).start() for i, t in procs.items()]