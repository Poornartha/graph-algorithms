'''
Single Source Shortest Path in a DAG using Topological Ordering.

Algorithm:

1. Initialize dist[] = {INF, INF, ….} and dist[s] = 0 where s is the source vertex.
2. Create a toplogical order of all vertices.
3. Do following for every vertex u in topological order.

    for every adjacent node v of u:
        if dist[v] > dist[u] + weight[u, v]:
            dist[v] = dist[u] + weight[u, v]

'''

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def topologicalSortUtil(self, v, visited, order):

        visited[v] = True

        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node, visited, order)

        order.append(v)

    def shortestPath(self, s):

        visited = [False] * self.v
        order = []

        for i in range(self.v):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, order)

        dist = [float('Inf')] * self.v
        dist[s] = 0
        order_cpy = order[::-1]

        while order:

            i = order.pop()

            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        print("N D")
        for i in range(self.v):
            print(order_cpy[i], dist[i])


g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

# source = 1
s = 1
  
print ("Following are shortest distances from source %d " % s)
g.shortestPath(s)
            



