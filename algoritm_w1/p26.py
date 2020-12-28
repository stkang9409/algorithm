n = int(input())

dp = [1] * (n+1)
if n > 1:
    for i in range(2, n+1):
        dp[i] = i*dp[i-1]

print(dp[n])
