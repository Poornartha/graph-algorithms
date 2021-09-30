'''
Dynamic Programming Approach to solve Travelling Salesman Problem

'''

def DP_TSP(distances_array):
  n = len(distances_array)
  all_points_set = set(range(n))
  
  # memo keys: tuple(sorted_points_in_path, last_point_in_path)
  # memo values: tuple(cost_thus_far, next_to_last_point_in_path)
  memo = {(tuple([i]), i): tuple([0, None]) for i in range(n)}
  queue = [(tuple([i]), i) for i in range(n)]
  
  while queue:
    prev_visited, prev_last_point = queue.pop(0)
    prev_dist, _ = memo[(prev_visited, prev_last_point)]
    to_visit = all_points_set.difference(set(prev_visited))
    
    for new_last_point in to_visit:
      new_visited = tuple(sorted(list(prev_visited) + [new_last_point]))
      new_dist = (prev_dist + distances_array[prev_last_point][new_last_point])
      
      if (new_visited, new_last_point) not in memo:
        memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
        queue += [(new_visited, new_last_point)]
      else:
        if new_dist < memo[(new_visited, new_last_point)][0]:
          memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
          
  optimal_path, optimal_cost = retrace_optimal_path(memo, n)
  return optimal_path, optimal_cost

def retrace_optimal_path(memo, n):
    points_to_retrace = tuple(range(n))
    print(memo)
    full_path_memo = dict((k, v) for k, v in memo.items() if k[0] == points_to_retrace)
    path_key = min(full_path_memo.keys(), key=lambda x: full_path_memo[x][0])

    last_point = path_key[1]
    optimal_cost, next_to_last_point = memo[path_key]
    optimal_path = [last_point]

    points_to_retrace = tuple(sorted(set(points_to_retrace).difference({last_point})))

    while next_to_last_point is not None:
        last_point = next_to_last_point
        path_key = (points_to_retrace, last_point)
        _, next_to_last_point = memo[path_key]

    optimal_path = [last_point] + optimal_path
    return optimal_path, optimal_cost

if __name__ == '__main__':

    n = 4
    graph= [[ 0, 10, 15, 20 ],
            [ 10, 0, 35, 25 ],
            [ 15, 35, 0, 30 ],
            [ 20, 25, 30, 0 ]]

    optimal_path, optimal_cost = DP_TSP(graph)

    print(f"Optimal Cost: {optimal_cost}")
    print("Optimal Path:")
    print(optimal_path)
    