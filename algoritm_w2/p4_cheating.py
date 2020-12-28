import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort(key=lambda x: abs(x))
new = [0]*(N-1)
for i in range(1, N):
    new[i-1] = (nums[i-1], nums[i])
new.sort(key=lambda x: abs(sum(x)))
result = sorted(new[0])

print(result[0], result[1])
