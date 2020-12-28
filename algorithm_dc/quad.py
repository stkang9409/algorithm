import sys
input = sys.stdin.readline

N = int(input())
mat = [input() for _ in range(N)]
result = []


def inspect(x, y, l):
    count = 0
    for i in range(x, x+l):
        for j in range(y, y+l):
            if mat[i][j] == "1":
                count += 1
    if count == l**2:
        return 1
    elif count == 0:
        return 0
    else:
        return -1


def solve(x, y, l):
    if l == 1:
        result.append(str(mat[x][y]))
        return mat[x][y]

    if inspect(x, y, l) < 0:
        result.append("(")
        l = l//2
        cmd = [(0, 0), (0, l), (l, 0), (l, l)]

        count = 0
        for c in cmd:
            solve(x+c[0], y+c[1], l)
            count += 1
        result.append(")")
        return 1

    else:
        r = str(inspect(x, y, l))
        result.append(r)
        return r


solve(0, 0, N)
print("".join(result))
