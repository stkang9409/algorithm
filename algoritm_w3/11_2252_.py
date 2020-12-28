from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)


def solve():
    result = []

    q = deque([])
    for i in range(1, len(graph)):
        val = indegree[i]
        if not val:
            q.append(i)

    while q:
        i = q.popleft()
        result.append(i)
        for x in graph[i]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)

    print(" ".join(map(str, result)))


solve()
