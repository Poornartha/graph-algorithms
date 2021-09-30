'''
The given implementation of the TSP is Naive and it works as follows:

1. Consider city 1 as the starting and ending point. 
   Since the route is cyclic, we can consider any point as a starting point.

2. Generate all (n-1)! permutations of cities.

3. Calculate the cost of every permutation and keep track of the minimum cost permutation.

4. Return the permutation with minimum cost.

'''

from itertools import permutations
INF = float('Inf')

def TSP(graph, s, V):

    # Store all Vertex except the Source Vertex => Used for Gen Permutations
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path_cost = INF
    next_permutation = permutations(vertex)
    min_path = []

    for i in next_permutation:

        current_pathweight = 0
        temp = []

        k = s
        temp.append(k)
        for j in i:
            current_pathweight += graph[k][j]
            temp.append(j)
            k = j
        current_pathweight += graph[s][k]
        temp.append(s)

        if min_path_cost > current_pathweight:
            min_path_cost = min(min_path_cost, current_pathweight)
            min_path = temp

    return (min_path_cost, min_path)

if __name__ == '__main__':

    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(TSP(graph, s, 4))