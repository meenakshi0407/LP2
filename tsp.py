
def greedy_bfs_tsp(mat, start):
    visited = set()
    visited.add(start)
    path = [start]
    total_dist = 0

    while len(visited) < len(mat):

        curr_city = path[-1]
        unvisited = [i for i in range(len(mat)) if i not in visited]

        if not unvisited:
            break

        next_city = None
        min_dist = float('inf')

        for city in unvisited:
            if mat[curr_city][city] < min_dist:
                min_dist = mat[curr_city][city]
                next_city = city


        path.append(next_city)
        visited.add(next_city)
        total_dist += mat[curr_city][next_city]


    path.append(start)
    total_dist += mat[path[-2]][start]

    return path, total_dist


mat = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
start = 0
route, min_dist = greedy_bfs_tsp(mat, start)
print(min_dist)
print(route)
        
        
        
