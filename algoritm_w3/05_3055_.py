import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
navi = [list(input().rstrip()) for _ in range(R)]
w_visited = [[0]*C for _ in range(R)]
m_visited = [[0]*C for _ in range(R)]


def solve():
    cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    water = deque([])
    mouse = deque([])
    for i in range(R):
        for j in range(C):
            if navi[i][j] == "*":
                water.append((i, j))
            elif navi[i][j] == "S":
                mouse.append((i, j))

    t = 0
    while mouse:
        for _ in range(len(water)):
            cur_i, cur_j = water.popleft()
            if not w_visited[cur_i][cur_j]:
                navi[cur_i][cur_j] = "*"
                w_visited[cur_i][cur_j] = 1
                for c in cmd:
                    next_i, next_j = cur_i+c[0], cur_j+c[1]
                    if 0 <= next_i < R and 0 <= next_j < C and (navi[next_i][next_j] == "." or navi[next_i][next_j] == "S"):
                        water.append((next_i, next_j))

        for _ in range(len(mouse)):
            cur_i, cur_j = mouse.popleft()
            if not m_visited[cur_i][cur_j]:
                if navi[cur_i][cur_j] == "D":
                    return t
                if navi[cur_i][cur_j] != "*":
                    navi[cur_i][cur_j] = "S"
                    m_visited[cur_i][cur_j] = 1
                    for c in cmd:
                        next_i, next_j = cur_i+c[0], cur_j+c[1]
                        if 0 <= next_i < R and 0 <= next_j < C and (navi[next_i][next_j] == "." or navi[next_i][next_j] == "D"):
                            mouse.append((next_i, next_j))
        t += 1
    return "KAKTUS"


print(solve())
