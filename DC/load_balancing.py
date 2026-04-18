class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.idx = 0
        self.conns = {s: 0 for s in servers}

    def round_robin(self):
        s = self.servers[self.idx]
        self.idx = (self.idx + 1) % len(self.servers)
        return s

    def least_conn(self):
        s = min(self.conns, key=self.conns.get)
        self.conns[s] += 1
        return s

# Terminal Output Execution
servers = ["S1", "S2", "S3"]
lb = LoadBalancer(servers)

print("Round Robin:")
for _ in range(4): 
    print(lb.round_robin())

print("\nLeast Connections:")
# Manually simulate some connections to show it picking different servers
print("Assigned:", lb.least_conn()) # Picks S1 (0 connections)
print("Assigned:", lb.least_conn()) # Picks S2 (0 connections)