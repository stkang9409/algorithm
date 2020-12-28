import sys
input = sys.stdin.readline


N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve():
    visited = [[0]*M for _ in range(N)]
    stack = []
    count = 0

    for i in range(N):
        for j in range(M):
            if table[i][j] > 0 and not visited[i][j]:
                stack.append((i, j))
                count += 1
                if count >= 2:
                    return count
                while stack:
                    x, y = stack.pop()
                    if not visited[x][y]:
                        visited[x][y] = 1
                        for dx, dy in cmd:
                            nx, ny = x+dx, y+dy
                            if not(0 <= nx < N and 0 <= ny < M):
                                continue
                            if not visited[nx][ny]:
                                if table[nx][ny] <= 0:
                                    table[x][y] -= 1
                                elif table[nx][ny] > 0:
                                    stack.append((nx, ny))

    return count


count = 1
year = 0
while count == 1:
    count = solve()
    year += 1

if count == 0:
    print(0)
else:
    print(year-1)
