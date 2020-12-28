import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parts = [[] for _ in range(N+1)]
for _ in range(M):
    part, part_from, num = map(int, input().split())
    parts[part].append((part_from, num))
dp = [[] for _ in range(N+1)]

for i in range(N):
    if not parts[i]:
        ans = [0]*(N+1)
        ans[i] = 1
        dp[i] = ans


def solve(n):
    ans = [0]*(N+1)
    stack = []
    if parts[n]:
        for part in parts[n]:
            part_from, num = part
            stack.append((part_from, num))
        while stack:
            idx, num = stack.pop()
            if dp[idx]:
                for i in range(len(ans)):
                    ans[i] += dp[idx][i]*num
            else:
                for part in parts[idx]:
                    part_from, n = part
                    stack.append((part_from, n*num))
    else:
        ans[n] = 1
    return ans


for i in range(1, N+1):
    dp[i] = solve(i)

for i in range(1, N):
    if dp[-1][i]:
        print(i, dp[-1][i])
