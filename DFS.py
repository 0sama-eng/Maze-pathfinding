def solveMaze(maze):
    R, C = len(maze), len(maze[0])

    # Find start
    start = (0, 0)
    for r in range(R):
        for c in range(C):
            if maze[r][c] == "S":
                start = (r, c)
                break
        else:
            continue
        break
    else:
        return None

    # Stack for DFS
    stack = []
    stack.append((start[0], start[1], 0))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]

    while stack:
        coord = stack.pop()   # LIFO → DFS

        if visited[coord[0]][coord[1]]:
            continue

        visited[coord[0]][coord[1]] = True

        if maze[coord[0]][coord[1]] == "E":
            return "The Distance Is " + str(coord[2])

        for dir in directions:
            nr, nc = coord[0] + dir[0], coord[1] + dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]): continue
            stack.append((nr, nc, coord[2] + 1))

    return None

with open ("maze.txt") as f:
  maze = []
  for line in f:
    maze.append([i for i in line.strip("\n")])
  print(solveMaze(maze))