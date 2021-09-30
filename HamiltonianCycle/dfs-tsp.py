'''
Travelling Salesman Problem implementation using BackTracking

Algorithm:

1. Consider city 1 (let say 0th node) as the starting and ending point. 
   Since route is cyclic, we can consider any point as starting point.

2. Start traversing from the source to its adjacent nodes in dfs manner.

3. Calculate cost of every traversal and keep track of minimum cost and keep on updating the value of minimum cost stored value.

4. Return the permutation with minimum cost.

Complexity Analysis;

The time complexity for obtaining the DFS of the given graph is O(V+E) where V is the number of nodes and E is the number of edges.
Here DFS has been repeated for V times.
T Complexity = O(V * (V+E))
The space complexity for the same is O(V).



'''

INF = float('Inf')

def TSP(graph, visited, currPos, n, count, cost, path_cost, path):

    if (count == n and graph[currPos][0]):
        path.append(0)
        path_cost[cost + graph[currPos][0]] = path
        return

    for i in range(n):
        if visited[i] == False and graph[currPos][i]:
            
            visited[i] = True
            TSP(graph, visited, i, n, count+1, cost+graph[currPos][i], path_cost, path+[i])
            visited[i] = False
    
if __name__ == '__main__':

    n = 4
    graph= [[ 0, 10, 15, 20 ],
            [ 10, 0, 35, 25 ],
            [ 15, 35, 0, 30 ],
            [ 20, 25, 30, 0 ]]
    visited = [False for i in range(n)]
    visited[0] = True


    path_cost = {}

    TSP(graph, visited, 0, n, 1, 0, path_cost, [0])

    keys = list(path_cost.keys())
    min_cost = min(keys)
    
    print(f"Min Cost: {min_cost}")
    print("The Path is:")
    print(path_cost[min_cost])


