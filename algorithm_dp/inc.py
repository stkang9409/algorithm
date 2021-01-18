import sys
input = sys.stdin.readline


def solve():
    N = int(input())

    dp = [[0]*10 for _ in range(N+1)]
    dp[0] = [1]*10
    for i in range(1, N+1):
        for x in range(10):
            for j in range(x+1):
                dp[i][x] += dp[i-1][j]

    print(dp[-1][-1] % 10007)


solve()
