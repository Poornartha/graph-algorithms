
'''
Time Complexity of the Algorithm due to the use of a Heap Priority Queue: O (ElogV)

'''

import heapq as hq

class Graph():

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.v):
            print(node, "\t", dist[node])

    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def checkPQ(self, dist, visited, pq, source):

        # (dist, nodeIndex)

        hq.heapify(pq)
        minIndex = source

        while visited[minIndex]:
            dist, minIndex = pq.pop(0)

        return minIndex

    def djikstra(self, source):

        dist = [float('Inf')] * self.v
        dist[source] = 0
        visited = [False] * self.v
        pq = [(0, source)]
        prev = [None] * self.v

        for _ in range(self.v):

            u = self.checkPQ(dist, visited, pq, source)

            visited[u] = True

            for v in range(self.v):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    pq.append((dist[v], v))
                    prev[v] = u
            
        self.print_solution(dist)

        return (dist, prev)

    def findShortestPath(self, source, dest):
        dist, prev = self.djikstra(source)
        path = []
        
        if dist[dest] == float('Inf'):
            return path

        at = dest
        while at != None:
            at = prev[at]
            path.append(at)
        return path[::-1]

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
g.djikstra(0)
print(g.findShortestPath(0, 5))
