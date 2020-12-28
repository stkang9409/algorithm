import sys
input = sys.stdin.readline


def bfs():
    R, C = map(int, input().split())
    mat = [list(input().strip()) for _ in range(R)]
    cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 0
    point = set()
    point.add((0, 0, mat[0][0]))
    while point:
        a, b, way = point.pop()
        cnt = max(cnt, len(way))
        for x, y in cmd:
            ax, by = a+x, b+y
            if 0 <= ax < R and 0 <= by < C and mat[ax][by] not in way:
                point.add((ax, by, way+mat[ax][by]))
    return cnt


print(bfs())
