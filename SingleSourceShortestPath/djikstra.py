'''
Djikstra's Algoritm:
Single Source Shortest Path Algorithm 
For Graphs with Non-Negative Edges.

Algorithm Overview:

1. Maintain a 'dist' array where the distance to every node is +ve Infinity.
   Mark the dist[source] = 0

2. Maintain a PQ of Key Value Pairs of (NodeIndex, Distance).
   These pairs will tell you which node to visit based on the sorted min value.

3. Insert (s, 0) into the PQ and loop while PQ is not empty pulling out the next 
   most promising (nodeIndex, distance) pair.

4. Iterate over all edges outwards from the current node and relax each edge appending 
   a new (nodeIndex, distance) key value pair to the PQ for every relaxation.

Time Complexity of the implementation is O(V^2). 
If the input graph is represented using adjacency list, it can be reduced to O(E log V) with the help of binary heap. 

Note: Djikstra differs from Topological Sorting as it can find the SSSP for Cycles.
Dijkstra's algorithm is necessary for graphs that can contain cycles, because they can't be topologically sorted.

'''

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
    def minDistance(self, dist, visited):

        min = float('Inf')

        for v in range(self.v):
            if dist[v] < min and visited[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def djikstra(self, source):

        dist = [float('Inf')] * self.v
        dist[source] = 0
        visited = [False] * self.v

        for _ in range(self.v):

            u = self.minDistance(dist, visited)

            visited[u] = True

            for v in range(self.v):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
            
        self.print_solution(dist)

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


