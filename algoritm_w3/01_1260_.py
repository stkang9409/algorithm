import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for v in graph:
    v.sort()


def dfs():
    stack = [V]
    result = []
    visited = {}
    while stack and len(result) < N:
        now = stack.pop()
        if not visited.get(now):
            result.append(now)
            visited[now] = True
            stack.extend(graph[now][::-1])
    print(" ".join(map(str, result)))


def bfs():
    que = deque([V])
    result = []
    visited = {}
    while que and len(result) < N:
        now = que.popleft()
        if not visited.get(now):
            result.append(now)
            visited[now] = True
            que.extend(graph[now])
    print(" ".join(map(str, result)))


dfs()
bfs()
