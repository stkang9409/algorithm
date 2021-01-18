import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solve():
    R, C = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(R)]
    cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dp = [[-1]*C for _ in range(R)]
    dp[-1][-1] = 1

    def dfs(i, j):
        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = 0
        for di, dj in cmd:
            ni, nj = i+di, j+dj
            if 0 <= ni < R and 0 <= nj < C:
                if graph[i][j] > graph[ni][nj]:
                    dp[i][j] += dfs(ni, nj)
        return dp[i][j]

    print(dfs(0, 0))


solve()
