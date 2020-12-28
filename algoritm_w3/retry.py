import sys


def solve():
    R, C = map(int, input().split())
    iceburg = [list(map(int, input().split())) for _ in range(R)]
    stack = []
    cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    year = 0
    count = 1
    while count == 1:
        visited = [[0]*C for _ in range(R)]
        count = 0

        for i in range(R):
            for j in range(C):
                if iceburg[i][j] > 0 and not visited[i][j]:
                    count += 1
                    stack.append((i, j))
                    while stack:
                        i, j = stack.pop()
                        if not visited[i][j]:
                            for a, b in cmd:
                                ai, bj = i+a, j+b
                                if not (0 <= ai < R and 0 <= bj < C):
                                    continue
                                if iceburg[ai][bj] <= 0 and not visited[ai][bj]:
                                    iceburg[i][j] -= 1

                            visited[i][j] = 1
                            for a, b in cmd:
                                ai, bj = i+a, j+b
                                if not (0 <= ai < R and 0 <= bj < C):
                                    continue
                                if iceburg[ai][bj] > 0 and not visited[ai][bj]:
                                    stack.append((ai, bj))

        year += 1

    if count == 0:
        return 0
    else:
        return year-1


print(solve())
