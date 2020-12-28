N = int(input())
arr = list(map(int, input().split()))
count = 0

check = [True] * 1001
check[0], check[1] = False, False

for n in range(2, 1001):
    if check[n]:
        i = n*2
        while i < len(check):
            check[i] = False
            i += n

for i in arr:
    if len(check) > i and check[i]:
        count += 1

print(count)
