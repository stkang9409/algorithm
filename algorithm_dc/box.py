import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
dp = [0]*20
for _ in range(int(input())):
    size, num = map(int, input().split())
    dp[size] = num
count = [0]
result = [0]


def solve(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return
    nums = [a, b, c]
    nums.sort()
    a, b, c = nums
    tmp = 1
    idx = 0
    while (tmp << 1) <= a:
        tmp = tmp << 1
        idx += 1

    while idx >= 0:
        if dp[idx] == 0:
            idx -= 1
            continue
        else:
            break

    tmp = 2**idx
    dp[idx] -= 1
    count[0] += 1
    result[0] += tmp**3

    solve(a, b, c-tmp)
    solve(a, b-tmp, tmp)
    solve(a - tmp, tmp, tmp)


solve(a, b, c)
if result[0] == a*b*c:
    print(count[0])
else:
    print(-1)
