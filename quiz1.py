import sys
read = sys.stdin.readline
goal, trap = map(int, read().rstrip().split())
dp = {}
for _ in range(trap):
    dp[int(read())] = True
maxSpeed = int(1.414*goal**(0.5))+1
memo = [[float('inf') for _ in range(goal+1)]
        for _ in range(maxSpeed)]
#속도, 위치
memo[1][1] = 0
for c in range(1, goal):
    if dp.get(c):
        continue
    for r in range(1, maxSpeed):
        if memo[r][c] is not float('inf'):
            if c+r > goal:
                continue
            memo[r][c+r] = min(memo[r][c+r], memo[r][c] + 1)
            if r+1 >= maxSpeed:
                continue
            memo[r+1][c+r] = min(memo[r+1][c+r], memo[r][c] + 1)
            if r-1 < 0:
                continue
            memo[r-1][c+r] = min(memo[r-1][c+r], memo[r][c] + 1)
# for i in memo:
#     print(i)
ans = float('inf')
for i in range(maxSpeed):
    ans = min(ans, memo[i][-1])
if ans == float('inf'):
    print(-1)
else:
    print(ans)
