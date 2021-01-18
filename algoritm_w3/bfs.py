import sys
from collections import deque

input = sys.stdin.readline


def solve():
    eat = 0
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    cmd = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if table[i][j] == 9:
                q.append((i, j, 2))
                table[i][j] = 0
                visited[i][j] = 1

    result = 0
    count = 0
    while q:
        count += 1
        candidate = []
        for _ in range(len(q)):
            ci, cj, csize = q.popleft()
            for a, b in cmd:
                ni, nj = a+ci, b+cj

                if not(0 <= ni < N and 0 <= nj < N):
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                if 0 < table[ni][nj] <= csize-1:
                    candidate.append((ni, nj))

                if table[ni][nj] <= csize:
                    q.append((ni, nj, csize))

        if candidate:
            candidate.sort(key=lambda x: (x[0], x[1]))
            ni, nj = candidate[0]
            table[ni][nj] = 0
            eat += 1
            result = count
            q.clear()
            visited = [[0]*N for _ in range(N)]
            if eat == csize:
                eat = 0
                csize += 1
            q.append((ni, nj, csize))

    return result


print(solve())
