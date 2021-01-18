import sys
input = sys.stdin.readline


def solve():
    str1 = input().rstrip()
    str2 = input().rstrip()
    l1 = len(str1)
    l2 = len(str2)
    dp = [[0]*(l1+1) for _ in range(l2+1)]  # [l2][l1]

    for i in range(1, l2+1):
        for j in range(1, l1+1):
            if str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    print(dp[-1][-1])


solve()
