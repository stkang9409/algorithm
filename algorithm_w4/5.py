import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    row = [0]*N
    col = [0]*N
    dp = [[float('inf')]*N for _ in range(N)]

    for i in range(N):
        row[i], col[i] = map(int, input().split())
        dp[i][i] = 0

    for j in range(1, N):
        for start in range(N-j):
            end = start+j
            result = float('inf')
            for k in range(start, end):
                result = min(result,
                             dp[start][k]+dp[k+1][end] + row[start]*col[k]*col[end])

            dp[start][end] = result

    print(dp[0][-1])


solve()
