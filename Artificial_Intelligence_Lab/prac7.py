from collections import deque

def find_start_end(maze):
    start = end = None
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == 'S':
                start = (r, c)
            elif val == 'E':
                end = (r, c)
    return start, end

def is_valid(r, c, rows, cols, maze, visited):
    return (0 <= r < rows and 0 <= c < cols and
            maze[r][c] != '#' and (r, c) not in visited)

def print_path(maze, path):
    maze_copy = [list(row) for row in maze]  # deep copy
    for r, c in path:
        if maze_copy[r][c] not in ('S', 'E'):
            maze_copy[r][c] = '*'
    for row in maze_copy:
        print(''.join(row))

def bfs(maze):
    start, end = find_start_end(maze)
    if not start or not end:
        print("Start or End point not found in maze.")
        return None

    rows, cols = len(maze), len(maze[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, maze, visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

def dfs(maze):
    start, end = find_start_end(maze)
    if not start or not end:
        print("Start or End point not found in maze.")
        return None

    rows, cols = len(maze), len(maze[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    stack = [(start, [start])]
    visited = set([start])

    while stack:
        (r, c), path = stack.pop()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, maze, visited):
                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))
    return None

# Sample Maze
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', '#', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

print("Maze solving using BFS:")
path_bfs = bfs(maze)
if path_bfs:
    print_path(maze, path_bfs)
else:
    print("No path found using BFS.")

print("\nMaze solving using DFS:")
path_dfs = dfs(maze)
if path_dfs:
    print_path(maze, path_dfs)
else:
    print("No path found using DFS.")

