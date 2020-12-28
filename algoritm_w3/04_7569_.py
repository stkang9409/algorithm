import sys
from collections import deque

input = sys.stdin.readline

col_n, row_n, box_n = map(int, input().split())

boxs = []
for _ in range(box_n):
    box = []
    for _ in range(row_n):
        row = list(map(int, input().split()))
        box.append(row)
    boxs.append(box)


def solve():
    visited = [[[0]*col_n for _ in range(row_n)] for _ in range(box_n)]
    que = deque([])
    cmd = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    result = 0
    for a in range(len(boxs)):
        for b in range(len(boxs[a])):
            for c in range(len(boxs[a][b])):
                if boxs[a][b][c] == 1:
                    que.append((a, b, c, 0))

    while que:
        cur_a, cur_b, cur_c, cur_day = que.popleft()
        boxs[cur_a][cur_b][cur_c] = 1
        if visited[cur_a][cur_b][cur_c] == 0:
            visited[cur_a][cur_b][cur_c] = 1
            for l, f, u in cmd:
                next_a, next_b, next_c = cur_a+l, cur_b+f, cur_c+u
                next_day = cur_day + 1
                if 0 <= next_a < box_n and 0 <= next_b < row_n and 0 <= next_c < col_n and boxs[next_a][next_b][next_c] == 0 and visited[next_a][next_b][next_c] == 0:
                    que.append((next_a, next_b, next_c, next_day))
                else:
                    result = max(result, cur_day)

    for a in range(len(boxs)):
        for b in range(len(boxs[a])):
            for c in range(len(boxs[a][b])):
                if boxs[a][b][c] == 0:
                    return -1

    return result


print(solve())
