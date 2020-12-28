import sys

input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
paper_count = [0, 0, 0]


def check(x, y, l):
    paper_type = mat[x][y]
    for i in range(x, x+l):
        for j in range(y, y+l):
            if mat[i][j] != paper_type:
                return False
    return True


def solve(x, y, l):
    is_paper = check(x, y, l)

    if is_paper:
        paper_count[mat[x][y]+1] += 1
        return

    gap = l//3
    cmds = [[0, 0], [gap, 0], [gap*2, 0], [0, gap], [gap, gap],
            [gap*2, gap], [0, gap*2], [gap, gap*2], [gap*2, gap*2]]

    for cmd in cmds:
        solve(x+cmd[0], y+cmd[1], gap)


solve(0, 0, N)
print("\n".join(map(str, paper_count)))
