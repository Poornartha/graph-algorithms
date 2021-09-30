# Recursive function to print the path of given vertex `u` from source vertex `v`
def printPath(path, v, u):
 
    if path[v][u] == v:
        return
 
    printPath(path, v, path[v][u])
    print(path[v][u], end=' ')
 
 
# Function to print the shortest cost with path
# information between all pairs of vertices
def printSolution(path, N):
 
    for v in range(N):
        for u in range(N):
            if u != v and path[v][u] != -1:
                print(f"The shortest path from {v} —> {u} is ({v}", end=' ')
                printPath(path, v, u)
                print(f"{u})")
 
 
# Function to run the Floyd–Warshall algorithm
def floydWarshall(adjMatrix, N):
 
    # cost and parent matrix stores shortest path
    # (shortest-cost/shortest route) information
 
    # initially, cost would be the same as the weight of an edge
    cost = adjMatrix.copy()
    path = [[None for x in range(N)] for y in range(N)]
 
    # initialize cost and parent
    for v in range(N):
        for u in range(N):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1
 
    # run Floyd–Warshall
    for k in range(N):
        for v in range(N):
            for u in range(N):
                # If vertex `k` is on the shortest path from `v` to `u`,
                # then update the value of `cost[v][u]` and `path[v][u]`
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]
 
            # if diagonal elements become negative, the
            # graph contains a negative-weight cycle
            if cost[v][v] < 0:
                print("Negative-weight cycle found")
                return
 
    # Print the shortest path between all pairs of vertices
    printSolution(path, N)
 
 
if __name__ == '__main__':
 
    # Total number of vertices in the `adjMatrix`
    N = 4
    I = float('inf')
 
    # given adjacency representation of the matrix
    adjMatrix = [
        [0, I, -2, I],
        [4, 0, 3, I],
        [I, I, 0, 2],
        [I, -1, I, 0]
    ]
 
    # Run Floyd–Warshall algorithm
    floydWarshall(adjMatrix, N)