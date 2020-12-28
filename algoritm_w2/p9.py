import sys
input = sys.stdin.readline


def solve():
    stack = []
    max_size = 0

    for i in range(len(rects)):
        start_point = i
        while stack and stack[-1][0] > rects[i]:
            height, start_point = stack.pop()
            max_size = max(max_size, height*(i-start_point))
        stack.append([rects[i], start_point])

    for height, start_point in stack:
        max_size = max(max_size, height*(len(rects)-start_point))

    return max_size


while True:
    N, *rects = map(int, input().split())
    if N != 0:
        print(solve())
    else:
        break
