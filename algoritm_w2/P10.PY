import sys
input = sys.stdin.readline


def product2(mat1):
    result = [[0]*len(mat1) for _ in range(len(mat1))]

    for c in range(len(mat1)):
        for j in range(len(mat1)):
            value = 0
            for i in range(len(mat1)):
                value += mat1[c][i]*mat1[i][j]
            result[c][j] = value % 1000

    return result


def product(mat1, mat2):
    result = [[0]*len(mat1) for _ in range(len(mat1))]

    for c in range(len(mat1)):
        for j in range(len(mat1)):
            value = 0
            for i in range(len(mat1)):
                value += mat1[c][i]*mat2[i][j]
            result[c][j] = value % 1000

    return result


def power_mat(mat, n):
    if n == 1:
        return mat

    if n % 2 == 0:
        return product2(power_mat(mat, n//2))
    return product(power_mat(mat, n-1), mat)


l, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(l)]

result = power_mat(mat, n)

for row in range(2):
    for i in range(2):
        result[row][i] %= 1000

for row in result:
    print(" ".join(map(str, row)))
