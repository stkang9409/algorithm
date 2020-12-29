import sys
from heapq import heappop, heappush


def solve(N):
    graph = []
    cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = [[float('inf')]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for _ in range(N):
        r = list(map(int, input().split()))
        graph.append(r)

    table = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for a, b in cmd:
                ai, bj = a+i, b+j
                if not (0 <= ai < N and 0 <= bj < N):
                    continue
                table[i][j].append(((ai, bj), graph[ai][bj]))
    q = []
    count[0][0] = graph[0][0]
    for coord, pay in table[0][0]:
        i, j = coord
        count[i][j] = min(count[i][j], pay + count[0][0])
        heappush(q, (pay, coord))
    visited[0][0] = 1

    while q:
        pay, coord = heappop(q)
        i, j = coord
        if visited[i][j]:
            continue
        visited[i][j] = 1
        for n_coord, n_pay in table[i][j]:
            ni, nj = n_coord
            count[ni][nj] = min(count[ni][nj], count[i][j]+n_pay)
            if not visited[ni][nj]:
                heappush(q, (count[ni][nj], (ni, nj)))
    return count[N-1][N-1]


t = 1
while True:
    N = int(input())
    if N == 0:
        break
    print(f"Problem {t}: {solve(N)}")
    t += 1
