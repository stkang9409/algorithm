import sys
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    lte = [[] for _ in range(N+1)]
    gte = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        lte[a].append(b)
        gte[b].append(a)

    count = 0
    stack = []
    for i in range(1, N+1):
        way = set()
        for j in gte[i]:
            stack.append(j)
        while stack:
            idx = stack.pop()
            way.add(idx)
            for x in gte[idx]:
                if x not in way:
                    stack.append(x)
            if len(way) > N//2:
                count += 1
                stack = []
                break

    stack = []

    for i in range(1, N+1):
        way = set()
        for j in lte[i]:
            stack.append(j)
        while stack:
            idx = stack.pop()
            way.add(idx)
            for x in lte[idx]:
                if x not in way:
                    stack.append(x)
            if len(way) > N//2:
                count += 1
                stack = []
                break

    return count


print(solve())
