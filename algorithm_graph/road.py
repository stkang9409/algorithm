import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solve():
    N, M, K = map(int, input().split())
    graph = [[(i, 0)] for i in range(N)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))

    visited = [[0]*N for _ in range(K+1)]
    dist = [[float('inf')]*N for _ in range(K+1)]  # [k][i]

    q = []
    dist[0][0] = 0
    q.append((dist[0][0], 0, 0))

    while q:
        cw, k, c = heappop(q)
        if visited[k][c]:
            continue
        visited[k][c] = 1
        for n, nw in graph[c]:
            if not visited[k][n] and dist[k][n] > dist[k][c]+nw:
                dist[k][n] = dist[k][c]+nw
                heappush(q, (dist[k][n], k, n))
            if k < K:
                if not visited[k+1][n] and dist[k+1][n] > dist[k][c]:
                    dist[k+1][n] = dist[k][c]
                    heappush(q, (dist[k+1][n], k+1, n))
        if visited[K][-1]:
            break
    print(dist[K][-1])


solve()
