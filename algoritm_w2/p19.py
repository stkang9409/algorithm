n, k = map(int, input().split())
num = input()


def build(num, k, n):
    target = n - k
    count = 0
    stack = []
    for n in num:
        if not stack or count == k:
            stack.append(n)
            continue

        while stack and count < k and stack[-1] < n:
            stack.pop()
            count += 1

        stack.append(n)
    result = "".join(stack)[:target]
    return result if result else 0


print(build(num, k, n))
