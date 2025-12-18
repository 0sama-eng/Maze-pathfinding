from heapq import heappush, heappop


def solveMazeAStar(maze):
    R, C = len(maze), len(maze[0])

    start = None
    end = None

    # Find S and E
    for r in range(R):
        for c in range(C):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "E":
                end = (r, c)

    if start is None or end is None:
        return None

    # Heuristic: Manhattan distance
    def h(r, c):
        return abs(r - end[0]) + abs(c - end[1])

    # Priority queue: (f, g, r, c)
    pq = []
    heappush(pq, (h(start[0], start[1]), 0, start[0], start[1]))

    visited = [[False] * C for _ in range(R)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while pq:
        f, g, r, c = heappop(pq)

        if visited[r][c]:
            continue
        visited[r][c] = True

        if (r, c) == end:
            return "The Distance Is " + str(g)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]): continue

            ng = g + 1
            nf = ng + h(nr, nc)
            heappush(pq, (nf, ng, nr, nc))

    return "No Path Found"


# Read maze from file
with open("maze.txt") as f:
    maze = [list(line.strip()) for line in f]

print(solveMazeAStar(maze))
