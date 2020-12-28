N = int(input())


def check(n):
    if n < 100:
        return True

    nums = []
    while n > 0:
        nums.append(n % 10)
        n = n//10
    gap = nums[1] - nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] != gap:
            return False

    return True


count = 0
for i in range(1, N+1):
    if check(i):
        count += 1

print(count)
