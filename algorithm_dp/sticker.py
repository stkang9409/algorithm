import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    dp = [[0]*3 for _ in range(N)]
    dp[0][0] = nums1[0]
    dp[0][1] = nums2[0]
    for i in range(1, N):
        for j in range(3):
            if j == 0:
                dp[i][j] = max(dp[i-1][1], dp[i-1][2]) + nums1[i]
            elif j == 1:
                dp[i][j] = max(dp[i-1][0], dp[i-1][2]) + nums2[i]
            else:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    print(max(dp[-1]))


for _ in range(int(input())):
    solve()
