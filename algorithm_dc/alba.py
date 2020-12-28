import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
stack = []
i = 0
result = 0

for num in nums:
    idx = i

    while stack and stack[-1][0] >= num:
        val, idx = stack.pop()
        result = max(result, val*(i-idx))

    stack.append([num, idx])
    i += 1

while stack:
    val, idx = stack.pop()
    result = max(result, val*(N-idx))

print(result)
