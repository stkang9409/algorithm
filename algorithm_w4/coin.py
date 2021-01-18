import sys

input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    dp = [0]*(K+1)
    nums = [0] * (N+1)
    for i in range(1, N+1):
        nums[i] = int(input())

    dp[0] = 1
    for i in range(1, N+1):  # 동전가치
        for j in range(1, K+1):  # 배낭크기
            if nums[i] <= j:  # 동전가치가 배낭보다 작거나 같으면
                dp[j] += dp[j-nums[i]]

    print(dp[-1])


solve()
