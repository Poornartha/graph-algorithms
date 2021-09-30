'''
Bellman Ford Algorithm:
Single Source Shortest Path Algorithm

Time Complexity: O(EV) 

It is better to use Dijkstra's Algorithm
with PQ as Time Complexity for that is O((E+V)log(V))

When to use Bellman Ford?
Djikstra's Algorithm fails when there are negative edge weights.
This is when BF is used as it can detect negative cycles and determine when they occur.

Negative Cycles:
1. Self Loop with Negative Edge Weight.
2. Loop wherein the net gain is negative (Example: Loop with edges 4, 1, -6)

Algorithm:
1. Set Dist[all nodes in the graph] = INF
2. Set Dist[source] = 0

3. Relax Each Edge V-1 Times:
   Relaxing an Edge = Updating the value 
   for numVertices - 1:
        for all edges:
            if (Dist[edge.from] + Dist[edge.cost]) < Dist[edge.to]:
                Dist[edge.to] = Dist[edge.from] + Dist[edge.cost]

4. In order to detect Negative Cycles we will relax the nodes again.
   Positive Cycles would not update as they are already the best possible dist.
   However, Megative Cycle would always update.
   This will help us identify negative cycles.

'''

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        # Edge List
        self.graph = []

    def addEdge(self, s, d, weight):
        self.graph.append((s, d, weight))

    def printUtil(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

    def BellmanFord(self, source):

        dist = [float('Inf')] * self.V
        dist[source] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                print(f"Negative Cycle Detected with Edge: {u} to {v}")
                return

        self.printUtil(dist)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.BellmanFord(0)

    

    
