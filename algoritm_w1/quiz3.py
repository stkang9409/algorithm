N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input().split()))


expected = [0, 0, 0]
candidate = []
ans = []


def combination(n, start, end=[], dp=[]):
    if n == 0:
        dp.append(end)
    for i in range(3):
        dp = combination(n-1, start[:i]+start[i+1:], end+start[i:i+1], dp)
    return dp


def inspect(info):
    nums = list(str(info[0]))
    strike = info[1]
    ball = info[2]
    certains = []
    balls = []

    if strike == 3 or ball == 2 and strike == 1:
        ans[0] = 1

    if ball:
        balls.extend(nums)
    for i in range(3):
        if strike == 1:
            combination(1, nums)
            combination(1, nums[:i])
        elif strike == 2:
            combination(2, nums)

    print(certains, balls)


for i in arr:
    inspect(i)
