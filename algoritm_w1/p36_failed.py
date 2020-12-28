def permutation(start, end=[], dp=[]):
    if len(start) == 0:
        dp.append(end)
    else:
        for i in range(len(start)):
            dp = permutation(start[:i] + start[i+1:], end + start[i:i+1], dp)
    return dp


N = int(input())
table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)


route = [i for i in range(N)]
routes = permutation(route)
for x in range(len(routes)):
    route = routes[x]
    coords = []
    for i in range(len(route)-1):
        if table[route[i]][route[i+1]] != 0:
            coords.append((route[i], route[i+1]))
    coords.append((route[-1], route[0]))
    if len(coords) == N:
        routes[x] = coords
    else:
        routes[x] = False


result = float('inf')
for coords in routes:
    if coords:
        total_pay = 0
        for coord in coords:
            total_pay += table[coord[0]][coord[1]]
        result = min(result, total_pay)

print(result)
