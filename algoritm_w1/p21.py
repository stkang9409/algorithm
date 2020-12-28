u, d, h = map(int, input().split())

one_day = u - d
count = 1
h = h-u

if h % one_day == 0:
    count += h//one_day
else:
    count += h//one_day + 1

print(count)
