import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline


def solve():
    city_num = int(input())
    bus_num = int(input())
    graph = [[] for _ in range(city_num+1)]
    dist = [float('inf')]*(city_num+1)

    for _ in range(bus_num):
        f, t, pay = map(int, input().split())
        graph[f].append((t, pay))

    start, end = map(int, input().split())
    q = []
    visited = [0]*(city_num+1)
    visited[start] = 1
    dist[start] = 0

    for t, pay in graph[start]:
        dist[t] = min(dist[t], pay)
        heappush(q, (pay, t))

    while q:
        pay, t = heappop(q)
        if visited[t]:
            continue
        if t == end:
            break
        visited[t] = 1
        for nt, np in graph[t]:
            dist[nt] = min(dist[nt], dist[t]+np)
            if not visited[nt]:
                heappush(q, (dist[nt], nt))

    return dist[end]


print(solve())
