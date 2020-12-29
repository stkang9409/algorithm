"""
다익스트라 알고리즘
1. 시작점에서 시작한다.
 - 모든 노드를 거리 기준으로    우선순위 큐에 집어 넣는다.
2. 시작점과 이어진 모든 노드로 갈 수 있는 최단거리를 갱신한다. 
3. 이어진 모든 노드를 우선순위 큐에 집어 넣는다.

"""

import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline


def solve():
    V, E = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(V+1)]
    q = []
    dist = [float("inf")]*(V+1)
    visited = [0]*(V+1)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    visited[start] = 1
    dist[start] = 0

    for v, w in graph[start]:
        dist[v] = min(dist[v], w)
        heappush(q, (w, v))

    while q:
        w, v = heappop(q)
        if visited[v]:
            continue
        visited[v] = 1
        for a, b in graph[v]:
            dist[a] = min(dist[a], dist[v] + b)
            if not visited[a]:
                heappush(q, (dist[a], a))

    for i in dist[1:]:
        print(i if i != float('inf') else "INF")


solve()
