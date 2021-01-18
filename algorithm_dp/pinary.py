import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    dp = [0]*(N+1)
    if 0 < N < 3:
        print(1)
        return
    dp[1] = 1
    dp[2] = 1
    for i in range(3, N+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[-1])


solve()
