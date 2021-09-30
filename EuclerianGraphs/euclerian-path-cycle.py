'''

Eulerian Path is a path in graph that visits every edge exactly once. 
Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex.

A graph is called Eulerian if it has an Eulerian Cycle and
called Semi-Eulerian if it has an Eulerian Path.


An undirected graph has Eulerian cycle if following two conditions are true.
    1. All vertices with non-zero degree are connected. 
    We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path (we only consider all edges).
    2. All vertices have even degree.

An undirected graph has Eulerian Path if following two conditions are true.
    1. All vertices with non-zero degree are connected. 
    We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path (we only consider all edges).
    2. If zero or two vertices have odd degree and all other vertices have even degree. 
    Note that only one vertex with odd degree is not possible in an undirected graph 
    (sum of all degrees is always even in an undirected graph)

Algorithm:
In Eulerian path, each time we visit a vertex v, we walk through two unvisited edges with one end point as v. 
Therefore, all middle vertices in Eulerian Path must have even degree. 
For Eulerian Cycle, any vertex can be middle vertex, therefore all vertices must have even degree.

'''

from collections import defaultdict

class Graph:

    def __init__(self, vertices): 
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)


    '''
    Check if all non-zero degree vertices are connected.
    It mainly does dfs traversal starting from node with non-zero degree.
    '''
    def isConnected(self):

        visited = [False] * self.V

        # Find Vertex with non zero degree
        for i in range(self.V):
            if len(self.graph[i]) > 1:
                break
        
        # If there are no edges in the graph: return True
        if i == self.V - 1:
            return True

        self.DFSUtil(i, visited)

        # Check if all Non Zero Degree Nodes are visited.
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
        
        return True

    def isEuclerian(self):

        if self.isConnected() == False:
            return 0

        else:

            odd = 0
            
            for i in range(self.V):
                if len(self.graph[i]) % 2 != 0:
                    odd += 1

            '''If odd count is 2, then semi-eulerian.
            If odd count is 0, then eulerian
            If count is more than 2, then graph is not Eulerian
            Note that odd count can never be 1 for undirected graph'''
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0
            
       # Function to run test cases
    def test(self):
        res = self.isEuclerian()
        if res == 0:
            print ("graph is not Eulerian")
        elif res ==1 :
            print ("graph has a Euler path")
        else:
            print ("graph has a Euler cycle")

#Let us create and test graphs shown in above figures
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.test()
  
g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 0)
g2.test()
  
g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(1, 3)
g3.test()
  
#Let us create a graph with 3 vertices
# connected in the form of cycle
g4 = Graph(3)
g4.addEdge(0, 1)
g4.addEdge(1, 2)
g4.addEdge(2, 0)
g4.test()
  
# Let us create a graph with all veritces
# with zero degree
g5 = Graph(3)
g5.test()