import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [1]*N
    # i < j 이고 nums[i] > nums[j] 인 것들 중 d[i]가 최대인 값 + 1
    for i in range(N-1):
        for j in range(i+1, N):
            if nums[i] > nums[j]:
                dp[j] = max(dp[j], dp[i]+1)

    print(max(dp))


solve()
