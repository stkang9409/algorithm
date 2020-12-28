s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)
retval = [0, 0]

dp = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(l1):
    for j in range(l2):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            if dp[i+1][j+1] > retval[0]:
                retval = [dp[i+1][j+1], i+1]

print(retval[0])
print(s1[retval[1]-retval[0]:retval[1]])
