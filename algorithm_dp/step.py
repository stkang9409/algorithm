import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    dp = [[0]*11 for _ in range(N+1)]

    if N == 1:
        print(9)
        return

    dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    for i in range(2, N+1):
        for j in range(0, 10):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])

    print(sum(dp[-1]) % 1000000000)


solve()
