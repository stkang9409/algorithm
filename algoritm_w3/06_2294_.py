import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

nums = [int(input()) for _ in range(n)]
dp = [0]*100001


def solve(k):
    que = deque(nums[:])
    t = 1
    while que:
        for _ in range(len(que)):
            val = que.popleft()
            if val == k:
                return t
            else:
                for num in nums:
                    n = num+val
                    if not dp[n] and n <= k:
                        dp[n] = 1
                        que.append(n)
        t += 1
    return -1


print(solve(k))
