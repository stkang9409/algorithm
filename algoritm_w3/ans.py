import sys


def solve():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())

    link = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)
    parts = [0] * (n + 1)

    for _ in range(m):
        x, y, k = map(int, sys.stdin.readline().strip().split())
        link[x].append((y, k))
        inDegree[y] += 1

    stack = [n]
    parts[n] = 1  # 부품 개수 저장

    while stack:
        now = stack.pop()
        for num, cnt in link[now]:
            parts[num] += parts[now] * cnt
            inDegree[num] -= 1
            if inDegree[num] == 0:
                stack.append(num)

    for i in range(1, n + 1):
        if not link[i]:
            print(i, parts[i])


solve()
