'''
There are instances in the real world where in some events must occur before others.

For Example,
In order to build a program it is first required to build its dependencies and these
dependencies might depend on other dependencies to be built.

Topological Ordering: Ordering of nodes in a directed graph where for each directed edge 
from Node A to Node B, Node A appears before Node B.

The Topological Sort Algorithm, can find a topological ordering in O(V + E) time.

Note: Topological Orderings are NOT Unique.

The only Graphs that can have Topological Orderings are Directed Acyclic Graphs (Including Trees).

How to Verify if the Graph has Cycles / Not: Use Tarjan's Strongly Connected Components Algorithm.

For Trees: Level order traversal will yeild topological ordering of the tree.

Algorithm:

1. Pick an Unvisited Node.

2. Begining with the selected node, do a Depth First Search (DFS) 
   exploring only unvisited nodes.

3. On the recursive callback of the DFS, add the current node to the 
   topological ordering in the reverse order.

Time Complexity: O(V+E). 
The above algorithm is simply DFS with an extra stack. So time complexity is the same as DFS which is.
Auxiliary space: O(V). 
The extra space is needed for the stack.

Topological Sort of 5 4 2 3 1 0 implies that they must occur in that order in order to satisfy all the dependencies.

'''

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # DFS:
    def topologicalSortUtil(self, v, visited, order):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, order) 

        # Adding into the Ordering:
        order.append(v)

    def topologicalSort(self):

        visited = [False] * self.v
        order = []

        # For All Nodes (Even if disconnected)
        for i in range(self.v):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, order)

        print(order[::-1])

# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print ("Following is a Topological Sort of the given graph")
 
# Function Call
g.topologicalSort()

