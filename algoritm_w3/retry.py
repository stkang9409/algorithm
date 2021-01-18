import sys


def solve():
    N, M = map(int, input().split())
    iceburg = [list(map(int, input().split())) for _ in range(N)]  # [N][M]
    cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # 빙산 검사 하면서 빙산 녹이기

    year = 0
    count = 1
    stack = []
    while 0 < count < 2:
        count = 0
        visited = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if iceburg[i][j] > 0 and not visited[i][j]:
                    stack = [(i, j)]
                    count += 1
                if count == 2:
                    return year
                while stack:
                    i, j = stack.pop()
                    if visited[i][j]:
                        continue
                    visited[i][j] = 1
                    for a, b in cmd:
                        ni, nj = i+a, j+b
                        if not (0 <= ni < N and 0 <= nj < M):
                            continue
                        if not visited[ni][nj]:
                            if iceburg[ni][nj] <= 0:
                                iceburg[i][j] -= 1
                            else:
                                stack.append((ni, nj))
        year += 1

    return 0


print(solve())
