import sys
from heapq import heappush, heappop

import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline
city_num, bus_num = map(int, input().split())
graph = [[] for _ in range(city_num+1)]
for _ in range(bus_num):
    f, t, pay = map(int, input().split())
    graph[f].append((t, pay))
    graph[t].append((f, pay))

x, y = map(int, input().split())


def get_dist(start, end):
    q = []
    dist = [float('inf')]*(city_num+1)
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


def solve():
    result = float('inf')
    a = get_dist(1, x)
    b = get_dist(x, y)
    c = get_dist(y, city_num)
    result = min(result, a+b+c)
    a = get_dist(1, y)
    b = get_dist(y, x)
    c = get_dist(x, city_num)
    result = min(result, a+b+c)

    if result != float('inf'):
        return result
    else:
        return -1


print(solve())
