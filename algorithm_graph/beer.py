import sys
from collections import deque
input = sys.stdin.readline


def get_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1]-coord2[1])


def dfs(end, visited):
    if flag[0]:
        return 1
    if end == N+1:
        flag[0] = 1
        return 1

    result = 0
    for i in range(1, N+2):
        if not visited[i] and not dp[i] and get_distance(coords[end], coords[i]) <= 1000:
            visited[i] = 1
            result = max(result, dfs(i, visited))
            visited[i] = 0

    if not result:
        dp[end] = 1

    return result


for _ in range(int(input())):
    flag = [0]
    N = int(input())
    coords = [list(map(int, input().split())) for _ in range(N+2)]
    visited = [0 for _ in range(N+2)]
    dp = [0 for _ in range(N+2)]
    visited[0] = 1

    result = dfs(0, visited)

    if result:
        print("happy")
    else:
        print("sad")
