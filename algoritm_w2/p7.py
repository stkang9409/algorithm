import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
blue_white = [0, 0]


def check_mat(x, y, l):
    total = 0
    for i in range(x, x+l):
        for j in range(y, y+l):
            total += mat[i][j]

    if total == l**2:
        return 1
    elif total == 0:
        return 2
    else:
        return 0


def count(x=0, y=0, l=N):
    paper_type = check_mat(x, y, l)
    if paper_type == 1:
        blue_white[1] += 1
    elif paper_type == 2:
        blue_white[0] += 1
    else:
        l = l//2
        count(x, y, l)
        count(x + l, y, l)
        count(x, y + l, l)
        count(x+l, y+l, l)


count()
print("\n".join(map(str, blue_white)))
