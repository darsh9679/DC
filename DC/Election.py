class Node:
    def __init__(self, i):
        self.id, self.alive = i, True

    def election(self, nodes):
        print(f"\nNode {self.id} sends ELECTION")
        h = [n for n in nodes if n.id > self.id and n.alive]
        if h:
            for n in h:
                print(f"{self.id} -> {n.id} : ELECTION")
                print(f"{n.id} -> {self.id} : OK")
                n.election(nodes)
        else:
            print(f"\nNode {self.id} becomes COORDINATOR")
            for n in nodes:
                if n.alive and n.id != self.id:
                    print(f"{self.id} -> {n.id} : COORDINATOR")

nodes = [Node(i) for i in range(1, 6)]
nodes[4].alive = False
print("Node 5 has FAILED")
nodes[2].election(nodes)