'''
Alternate Implementation of DFS Bridges

'''

from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.low = [float('Inf')] * vertices
        self.ids = [float('Inf')] * vertices
        self.id = 0
        self.solved = False
        self.visited = [False] * vertices
        self.graph = defaultdict(list)
        self.bridges = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def findBridges(self):

        if self.solved:
            return self.bridges

        for i in range(self.V):
            if self.visited[i] == False:
                self.dfs(i, -1)

        self.solved = True

    def dfs(self, u, parent):

        self.visited[u] = True
        self.id += 1
        self.low[u] = self.ids[u] = self.id
        

        for v in self.graph[u]:

            if v == parent:
                continue

            if self.visited[v] == False:
                self.dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])
                if self.ids[u] < self.low[v]:
                    self.bridges.append(u)
                    self.bridges.append(v)
            else:
                self.low[u] = min(self.low[u], self.ids[v])

    def printBridges(self):

        for i in range(len(self.bridges)//2):
            node1 = self.bridges[2 * i]
            node2 = self.bridges[2 * i + 1]
            print(f"{node1} {node2}")


if __name__ == '__main__':

    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)

    print("Bridges in first graph ")
    g1.findBridges()
    g1.printBridges()

    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print("\nBridges in second graph ")
    g2.findBridges()
    g2.printBridges()

    g3 = Graph(7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    print("\nBridges in third graph ")
    g3.findBridges()
    g3.printBridges()
