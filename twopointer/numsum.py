import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    nums = list(map(int, input().split()))

    i = 0
    count = 0
    total = 0

    for x in range(len(nums)):
        num = nums[x]
        total += num

        while i <= x:
            if total < M:
                break
            elif total > M:
                total -= nums[i]
                i += 1
            else:
                count += 1
                break

    print(count)


solve()
