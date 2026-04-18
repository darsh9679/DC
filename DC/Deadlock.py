# Chandy-Misra-Haas Deadlock Detection
def send_probe(init, sender, receiver, visited, graph):
    # Base Case: Stop if we've already sent this probe
    if (sender, receiver) in visited: return False
    visited.add((sender, receiver))

    for next_site, is_waiting in enumerate(graph[receiver]):
        if is_waiting:
            print(f"P({init+1}, {receiver+1}, {next_site+1})")
            
            # Deadlock condition: Probe returns to the initiator
            if next_site == init: return True
            
            # Recursively forward the probe
            if send_probe(init, receiver, next_site, visited, graph): return True
    return False

# Setup for testing
graph = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
init = int(input("Enter Initiator Site (1-5): ")) - 1

print("\n--- Sending Probes ---")
if send_probe(init, init, init, set(), graph):
    print("RESULT: DEADLOCK DETECTED")
else:
    print("RESULT: NO DEADLOCK")