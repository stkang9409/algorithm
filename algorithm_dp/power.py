import sys
from math import sqrt
input = sys.stdin.readline


def solve():
    N = int(input())
    dp = [(N+2)]*(N+1)
    dp[0] = 0

    for i in range(1, N+1):
        tmp = N+1
        for j in range(1, int(pow(N, 0.5))+1):
            tmp = min(tmp, dp[i-j**2])
        dp[i] = tmp + 1

    print(dp[-1])


solve()
