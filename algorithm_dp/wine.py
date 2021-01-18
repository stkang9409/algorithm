import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    wines = [0]*N
    for i in range(N):
        wines[i] = int(input())

    if N == 1:
        print(wines[0])
        return
    if N == 2:
        print(wines[1]+wines[0])
        return
    dp = [0]*(N+1)
    dp[1] = wines[0]
    dp[2] = wines[1] + dp[0]

    for i in range(2, N+1):
        dp[i] = max(wines[i-1]+wines[i-2] + dp[i-3],
                    wines[i-1] + dp[i-2], dp[i-1])

    print(max(dp))


solve()
