import threading

graph = {1: [2], 2: [3], 3: [4], 4: []}  # distributed nodes waiting on each other

def detect():
    visited, stack, deadlock = set(), set(), [False]
    def dfs(n):
        visited.add(n); stack.add(n)
        for nb in graph.get(n, []):
            if nb not in visited: dfs(nb)
            elif nb in stack: print(f"Cycle {n}→{nb} | DEADLOCK 🔴"); deadlock[0]=True
        stack.discard(n)
    [dfs(n) for n in graph if n not in visited]
    print("No Deadlock ✅") if not deadlock[0] else print("System Halted 🛑")

print("Wait-For Graph:", graph)
threading.Thread(target=detect).start()