from collections import deque


def topological_sort():
    q = deque()
    N, M = int(input()), int(input())
    nodes = [[] for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    dp = [[0]*(N+1) for _ in range(N+1)]
    basic = []

    for _ in range(M):
        part, f, num = map(int, input().split())
        indegree[part] += 1
        graph[part].append([f, num])
        nodes[f].append(part)

    for i in range(1, N+1):
        if indegree[i] == 0:
            dp[i][i] = 1
            q.append(i)
            basic.append(i)

    while q:
        i = q.popleft()
        for x in nodes[i]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)
        for f, num in graph[i]:
            for j in range(1, N+1):
                dp[i][j] += dp[f][j]*num

    for i in basic:
        print(i, dp[-1][i])
    return


topological_sort()
