import sys

input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    dp = [[0]*(K+1) for i in range(N+1)]
    nums = [0] * (N+1)
    for i in range(1, N+1):
        nums[i] = int(input())
        dp[i][0] = 1

    for i in range(0, K+1):
        dp[0][i] = 1

    for i in range(1, N+1):  # 동전가치
        for j in range(1, K+1):  # 배낭크기
            if nums[i] <= j:  # 동전가치가 배낭보다 작거나 같으면
                for x in range(1, i+1):  # 동전보다 작거나 같은 모든 동전
                    dp[i][j] += dp[x][j-nums[x]]
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[-1][-1])


solve()
