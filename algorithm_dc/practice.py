N = int(input())
nums = list(map(int, input().split()+[0]))


def solve():
    stack = [()]
    cur = 0
    result = 0
    for num in nums:
        idx = cur
        while (num, cur) < stack[-1]:
            height, idx = stack.pop()
            result = max(result, (cur-idx)*height)

        stack.append((num, idx))
        cur += num
    print(result)


solve()
