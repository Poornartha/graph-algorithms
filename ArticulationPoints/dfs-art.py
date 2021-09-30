'''
Articulation Points are closely related to bridges. 

Observation:
On a Connected Component with three or more vertices 
if an edge (u, v) is a bridge then either u or v is an articulation point.

If a cycle exits in the graph such that 
id(end.from) == lowlink(end.to)
then,
The Vertex with the Outgoing Edge will be the Articulation Point.

Algorithm:

1. Using DFS we follow the vertices in tree form called DFS Tree.
2. In DFS Tree, a Vertex U is parent of another Vertex V. 
3. In DFS Tree, a vertex U is Articulation Point if one of the following 
   2 conditions is True.
    - U is root of the DFS Tree and it has at least 2 children.
    - U is not the root of DFS Tree and it has a Child V such that no vertex 
      in the subtree root with V has a back edge to one of the ancestors 
      (in DFS Tree) of U.

In DFS Traversal,
We maintain a parent[] array where array[u] stores parent vertex U.
For every vertex, we count Children.

If currently visited vertex U is root (i.e. parent[U] = None) and has 
more then 2 children, print it.

For Second Case,
We Maintain a array disc[] to store discovery times of vertices.
For every node U, we need to find out the earliest visited vertex 
that can be reached from subtree root U.
So, 
We maintain an additional array low[]
Such that,
low[u] = min(disc[u], disc[w])
Where w is an ancestor of u and there is a back edge from some descendant of u to w.

'''

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def APUtil(self, u, visited, ap, parent, low, disc):

        children = 0

        visited[u] = True

        disc[u] = self.Time
        low[u] = self.Time
        self.Time

        for v in self.graph[u]:

            if visited[v] == False:
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent,low, disc)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent:
                low[u] = min(low[u], disc[v])

    def AP(self):

        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.APUtil(i, visited, ap, parent, low, disc)

        for index, value in enumerate (ap):
            if value == True: 
                print(index)

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
  
print ("\nArticulation points in first graph ")
g1.AP()
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nArticulation points in second graph ")
g2.AP()
 
  
g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print( "\nArticulation points in third graph ")
g3.AP()
 

    

