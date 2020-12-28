N = int(input())
A = list(map(int, input().split()))
big = [A, ]

retval = 0


# 모든 순열 구하기

def permutations(start, end=[], dp=[]):
    if len(start) == 0:
        dp.append(end)
    else:
        for i in range(len(start)):
            dp = permutations(start[:i] + start[i+1:], end + start[i:i+1], dp)
    return dp


# 모든 순열 검사하기
for a in permutations(A):
    cache = 0
    for i in range(len(a)-1):
        cache += abs(a[i] - a[i+1])
    retval = max(retval, cache)

print(retval)
