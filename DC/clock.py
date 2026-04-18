import time, random
from multiprocessing import Process, Pipe

def node(n, conn, t):
    while True:
        msg = conn.recv()
        if msg == "GET":
            conn.send(t)
        elif msg == "STOP":
            break
        else:
            t += msg
            print(f"Node {n} adjusted by {msg:.2f} -> {t:.2f}")

def master(conns):
    for c in conns:
        c.send("GET")
    times = [c.recv() for c in conns]
    avg = sum(times) / len(times)
    offs = [avg - t for t in times]

    print("Times:", times)
    print("Avg:", round(avg, 2))
    print("Offsets:", [round(o, 2) for o in offs])

    for c, o in zip(conns, offs):
        c.send(o)
    time.sleep(1)
    for c in conns:
        c.send("STOP")

if __name__ == "__main__":
    ps, conns = [], []
    for i in range(4):
        p_conn, c_conn = Pipe()
        p = Process(target=node, args=(i + 1, c_conn, 10 + random.uniform(-2, 2)))
        ps.append(p)
        conns.append(p_conn)
        p.start()

    time.sleep(1)
    master(conns)

    for p in ps:
        p.join()