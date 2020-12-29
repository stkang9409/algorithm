import sys
from heapq import heappop, heappush
input = sys.stdin.readline

cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve():
    N, M = map(int, input().split())
    maze = []
    visited = [[0]*N for _ in range(M)]
    dist = [[float('inf')]*N for _ in range(M)]
    q = []
    for _ in range(M):
        maze.append(input().rstrip())

    visited[0][0] = 1
    dist[0][0] = int(maze[0][0])
    for a, b in cmd:
        if 0 <= a < M and 0 <= b < N:
            dist[a][b] = min(dist[a][b], dist[0][0]+int(maze[a][b]))
            heappush(q, (dist[a][b], a, b))

    while q:
        _, i, j = heappop(q)
        if visited[i][j]:
            continue
        visited[i][j] = 1
        for x, y in cmd:
            ix, jy = i+x, j+y
            if 0 <= ix < M and 0 <= jy < N and not visited[ix][jy]:
                dist[ix][jy] = min(dist[ix][jy], dist[i][j]+int(maze[ix][jy]))
                heappush(q, (dist[ix][jy], ix, jy))

    print(dist[-1][-1])


solve()
