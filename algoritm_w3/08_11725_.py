import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    graph = [[] for _ in range(N+1)]
    checked = [0]*(N+1)
    parent = [0]*(N+1)

    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    stack = [1]

    while stack:
        node = stack.pop()
        checked[node] = 1
        for num in graph[node]:
            if checked[num]:
                pass
            else:
                parent[num] = node
                stack.append(num)

    for node in range(2, N+1):
        print(parent[node])


solve()
