import threading, time

# Shared resource and lock
counter = 0
lock = threading.Lock()

def task(id):
    global counter
    for _ in range(3):
        print(f"P{id} waiting")
        
        with lock: # Handles acquire() and release() automatically
            print(f"P{id} in CS")
            temp = counter
            time.sleep(0.1) # Simulate work
            counter = temp + 1
            print(f"P{id} updated: {counter}")

# Create and start 5 threads
threads = [threading.Thread(target=task, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(f"Final Value: {counter}")