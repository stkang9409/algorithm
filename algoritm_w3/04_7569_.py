import sys
from collections import deque

R, C, H = map(int, input().split())
boxs = [[list(map(int, input().split())) for _ in range(C)]
        for _ in range(H)]  # [H][C][R]
visited = [[[0]*R for _ in range(C)] for _ in range(H)]
cmd = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), ]


def solve():
    result = 0
    count = 0
    q = deque()
    # 0 찾기
    for i in range(R):
        for j in range(C):
            for w in range(H):
                if boxs[w][j][i] == 1:
                    q.append((w, j, i))
                elif boxs[w][j][i] == 0:
                    count += 1

    # 익은 토마토 주변 익히기
    t = 0
    while q and count != result:
        for _ in range(len(q)):
            cw, cj, ci = q.popleft()
            for a, b, c in cmd:
                nw, nj, ni = cw+a, cj+b, ci+c
                if not(0 <= nw < H and 0 <= nj < C and 0 <= ni < R):
                    continue
                if boxs[nw][nj][ni] == 0:
                    result += 1
                    boxs[nw][nj][ni] = 1
                    q.append((nw, nj, ni))
        t += 1

    if count == result:
        return t
    else:
        return -1


print(solve())
