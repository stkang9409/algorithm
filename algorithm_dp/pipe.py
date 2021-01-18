import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    dp = [[(0, 0, 0)]*(N + 1) for i in range(N+1)]
    dp[1][2] = (1, 0, 0)
    for i in range(1, N+1):
        for j in range(2, N+1):
            if i == 1 and j == 2:
                continue
            if table[i-1][j-1]:
                continue

            if table[i-1][j-2]:
                x = 0
            else:
                x = dp[i][j-1][0] + dp[i][j-1][2]

            if table[i-2][j-1]:
                y = 0
            else:
                y = dp[i-1][j][1] + dp[i-1][j][2]

            if table[i-1][j-2] or table[i-2][j-1] or table[i-2][j-2]:
                z = 0
            else:
                z = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            dp[i][j] = (x, y, z)

    print(sum(dp[-1][-1]))


solve()
