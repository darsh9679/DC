import threading, time

c = [10, 12, 15]
print("Before:", c)

def sync():
    avg = sum(c) / len(c)
    offsets = [avg - t for t in c]
    for i, o in enumerate(offsets): c[i] += o
    print("Offsets:", [round(o,2) for o in offsets])
    print("After:", c)

threading.Thread(target=sync).start()