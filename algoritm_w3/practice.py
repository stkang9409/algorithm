import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [input().rstrip() for _ in range(N)]
cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve(N, M):
    que = deque([(0, 0, 1)])
    visited = [[0]*M for _ in range(N)]
    while que:
        i, j, value = que.popleft()
        if i == N-1 and j == M-1:
            return value
        if visited[i][j] == 0:
            visited[i][j] = 1
            for a, b in cmd:
                ni = i + a
                nj = j+b
                if not(0 <= ni < N and 0 <=)
