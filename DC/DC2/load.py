servers = ["S1", "S2", "S3"]
conns = {"S1": 2, "S2": 1, "S3": 0}
idx = 0

def round_robin():
    global idx
    s = servers[idx]; idx = (idx + 1) % len(servers); return s

def least_conn():
    s = min(conns, key=conns.get); conns[s] += 1; return s

print("Round Robin:")
[print(round_robin()) for _ in range(4)]

print("\nLeast Connections:")
[print("Assigned:", least_conn()) for _ in range(4)]
