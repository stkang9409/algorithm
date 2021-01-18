import sys
input = sys.stdin.readline


N, K = map(int, input().split())


def solve():
    dp = [[0]*(K+1) for _ in range(N+1)]
    weight = [0]*(N+1)
    value = [0]*(N+1)
    for i in range(1, N+1):
        w, v = map(int, input().split())
        weight[i] = w
        value[i] = v

    for i in range(1, N+1):
        for j in range(1, K+1):
            if j >= weight[i]:
                dp[i][j] = max(dp[i-1][j],
                               value[i] + dp[i-1][j-weight[i]])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])


solve()
