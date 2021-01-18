import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    steps = [int(input()) for _ in range(N)]
    if N == 1:
        print(steps[0])
        return
    elif N == 2:
        print(steps[1]+steps[0])
        return

    dp = [0]*N

    dp[0] = steps[0]
    dp[1] = steps[0]+steps[1]

    #점화식
    for i in range(2, N):
        dp[i] = max(dp[i-2] + steps[i], dp[i-3] + steps[i]+steps[i-1])

    print(dp[-1])


solve()
