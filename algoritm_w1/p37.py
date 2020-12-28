import copy

N = int(input())
RANGE = float("-inf")
area = [[0]*(N+2) for _ in range(N+2)]
arr_for_inspect = []

for i in range(1, N+1):
    row = list(map(int, input().split()))
    val = max(row)
    RANGE = max(val, RANGE) - 1
    area[i] = [0] + row + [0]
    arr_for_inspect.extend(row)

arr_set = sorted(set(arr_for_inspect))


def check(i, j, n, table):
    if table[i][j] > n:
        table[i][j] = float("-inf")

        if table[i+1][j] > n:
            check(i+1, j, n, table)

        if table[i-1][j] > n:
            check(i-1, j, n, table)

        if table[i][j+1] > n:
            check(i, j+1, n, table)

        if table[i][j-1] > n:
            check(i, j-1, n, table)


max_val = 0
for n in arr_set:
    count = 0
    table = copy.deepcopy(area)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if table[i][j] > n-1:
                check(i, j, n-1, table)
                count += 1
    max_val = max(count, max_val)


print(max_val)
