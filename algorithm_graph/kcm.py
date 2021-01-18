import sys
input = sys.stdin.readline


def pro():
    def solve(i, m, t):
        if m > M:
            return
        if i == N-1:
            min_val[0] = min(min_val[0], t)
            return
        for ni, nm, nt in graph[i]:
            if not visited[ni]:
                visited[ni] = 1
                solve(ni, m+nm, t+nt)
                visited[ni] = 0
        return
--
    for _ in range(int(input())):
        min_val = [float("inf")]
        N, M, K = map(int, input().split())
        graph = [[] for _ in range(N)]
        for _ in range(K):
            f, t, money, time = map(int, input().split())
            graph[f-1].append((t-1, money, time))
        visited = [0]*N
        visited[0] = 1
        solve(0, 0, 0)
        print(min_val[0] if min_val[0] != float('inf') else "Poor KCM")

pro()