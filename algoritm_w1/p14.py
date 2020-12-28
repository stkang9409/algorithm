dp = [0]*10

a = int(input())
b = int(input())
c = int(input())

prod_s = str(a*b*c)

for c in prod_s:
    n = int(c)
    dp[n] += 1

for val in dp:
    print(val)
