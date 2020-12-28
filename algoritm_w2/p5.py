# LIS
N = int(input())
nums = list(map(int, input().split()))
dp = []


def search(x):
    if not dp:
        dp.append(x)
        return

    if dp[-1] < x:
        dp.append(x)
        return

    start = 0
    end = len(dp) - 1

    while start <= end:
        middle = (start+end)//2

        if dp[middle] < x:
            start = middle + 1
        else:
            end = middle - 1

    dp[start] = x


for num in nums:
    search(num)

print(len(dp))
