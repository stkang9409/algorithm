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


def check(i, j, h, table):
    q = []
    q.append((i, j))
    if table[i][j] > h:
        table[i][j] = float("-inf")
    roads = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        x, y = q.pop(0)
        for next_x, next_y in roads:
            if table[x+next_x][y+next_y] > h:
                table[x+next_x][y+next_y] = float("-inf")
                q.append((x+next_x, y+next_y))


max_val = 0
for h in arr_set:
    count = 0
    table = copy.deepcopy(area)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if table[i][j] > h-1:
                check(i, j, h-1, table)
                count += 1
    max_val = max(count, max_val)


print(max_val)
