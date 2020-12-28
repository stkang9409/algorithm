N = int(input())
towers = list(map(int, input().split()))


def laser():
    stack = []
    result = [0]*N

    for i in range(len(towers)):
        if not stack:
            stack.append(i)
            continue

        while stack and towers[stack[-1]] < towers[i]:
            stack.pop()

        result[i] = stack[-1] + 1 if stack else 0
        stack.append(i)

    return result


print(" ".join(map(str, laser())))
