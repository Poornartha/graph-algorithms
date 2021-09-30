'''
Floyd Warshall is a All Pairs Shortest Path Algorithm.
It can find the shortest path between all pairs of nodes.

Time Complexity: O(V ^ 3)
Ideal for Graphs no larger than a couple of hundred nodes.

FW can detect negative cycles.

Best way to consume input for FW algorithm to represent it using a Adj Matrix.

If there is no edge between (i, j), mark is as INF in the Input Adj Matrix.

The main Idea behind FW is to build up all intermediate routes between nodes i and j.

if m[a][b] > m[a][c] + m[c][b] the it is better to go through node c.

Note that the Intermediate Nodes can be any number of Nodes and also Nodes that have not been computed.

Thus, we will use a Memo Table to cache the distances.

d[k][i][j] = Shortest path from i to j routing through nodes {0, 1, 2, ..., k}

Thus the approach is:
- Calculate the distances by routing through 0
- Calculate the distances by routing through 0, 1
- Calculate the distances by routing through 0, 1, 2
...
- Calculate the distances by routing through 0, 1, 2, ..., k

Specifically d[n-1] is the 2D Solution we want.

Thus, DP Solution:

Initially, 
dp[k][i][j] = m[i][j] if k = 0

Otherwise,
dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])
'''

class Graph:

    def __init__(self, vertices, adj_mat):
        self.V = vertices
        self.graph = adj_mat

    def printUtil(self, dist):
        print("Following matrix shows the shortest distances between every pair of vertices")
        for i in range(self.V):
            for j in range(self.V):
                if(dist[i][j] == float('Inf')):
                    print(f"{float('Inf')}\t", end=" ")
                else:
                    print(f"{dist[i][j]}\t", end=" ")
                if j == self.V-1:
                    print()

    def floydWarshall(self):

        dist = [self.graph[i][:] for i in range(self.V)]

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][j] != min(dist[i][j], dist[i][k] + dist[k][j]):
                        print(f"Negative Cycle found at Edge from {i} to {j}")
                        return
        
        self.printUtil(dist)

INF = float('Inf')
VERTICES = 5

graph = [[0, 5, INF, 2, INF],
         [INF, 0, 2, INF, INF],
         [3, INF, 0, INF, 7],
         [INF, INF, 4, 0, 1],
         [1, 3, INF, INF, 0]
         ]

g = Graph(VERTICES, graph)
source = 0
dest = 3

g.floydWarshall()

