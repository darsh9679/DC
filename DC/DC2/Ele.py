import threading

procs = [1,2,3,4,5,6]
failed = 5

def bully(n):
    if n == failed: return
    higher = [i for i in procs if i > n and i != failed]
    if higher:
        print(f"P{n} → ELECTION to {higher}, P{max(higher)} responds OK")
        threading.Thread(target=bully, args=(max(higher),)).start()
    else:
        print(f"P{n} → No higher process alive, P{n} is LEADER 👑")

threading.Thread(target=bully, args=(min(procs),)).start()