import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def pro():
    def check(max_val):
        for i in range(V):
            if dist[i] + dist1[i] == max_val:
                for v, p in graph[i]:
                    if (dist[i] + p) + dist1[v] == max_val:
                        candidate[i][v] = 1


    def solve(S, D, dist, graph):
        visited = [0]*(V+1)
        visited[S] = 1
        dist[S] = 0
        q = []

        for v, p in graph[S]:
            if not candidate[S][v]:
                dist[v] = min(dist[v], p)
                heappush(q, (dist[v], v))

        while q:
            p, v = heappop(q)
            if visited[v]:
                continue
            visited[v] = 1
            for nv, np in graph[v]:
                if not candidate[v][nv] and not visited[nv]:
                    dist[nv] = min(dist[nv], dist[v]+np)
                    heappush(q, (dist[nv], nv))
        return dist[D]


    while True:
        V, E = map(int, input().split())
        if V == 0 and E == 0:
            break
        S, D = map(int, input().split())
        graph = [[] for _ in range(V)]
        graph1 = [[] for _ in range(V)]
        dist = [float('inf')]*(V)
        dist1 = [float('inf')]*(V)
        for _ in range(E):
            u, v, p = map(int, input().split())
            graph[u].append((v, p))
            graph1[v].append((u, p))

        candidate = [[0]*V for _ in range(V)]

        max_val = solve(S, D, dist, graph)

        solve(D, S, dist1, graph1)
        check(max_val)
        dist = [float('inf')]*(V)

        ans = solve(S, D, dist, graph)

        if ans == float('inf'):
            print(-1)
        else:
            print(ans)
pro()
