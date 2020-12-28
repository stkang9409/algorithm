import sys

input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))


def bin_search(x, nums=nums, N=N):
    pl = x + 1
    pr = N-1
    result = float("inf")
    while pl <= pr:
        pc = (pl+pr)//2
        two_sum = nums[x] + nums[pc]

        if two_sum == 0:
            return nums[pc]
        if pc == x:
            break

        if abs(two_sum) < abs(result+nums[x]):
            result = nums[pc]

        if two_sum < 0:
            pl = pc + 1
        else:
            pr = pc - 1

    return result


def inspect(nums=nums):
    result = [float('inf'), float('inf')]
    for i in range(len(nums)-1):
        num = nums[i]
        counter = bin_search(i)
        if abs(counter+num) < abs(sum(result)):
            result = [num, counter]
    return result


print(" ".join(map(str, inspect())))
