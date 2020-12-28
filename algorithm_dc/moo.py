# dp 를 이용해 입력 길이가 들어가는 번호를 찾는다.
# 입력 길이가 해당 번호 더하기 중간 길이, 그리고 해당 번호 뒷 길이 둘 중 어디에 해당하는지 찾는다.

# 1. 해당 번호 중간 길이일 떄. ( 즉 입력길이에 해당번호 전 길이를 뺀 값이 중간 길이보다 짧을 때):
#     중간의 첫번째면 m
#     아니면 o
# 2. 해당 번호의 뒷부분일 때
#     입력길이에 중간길이 와 앞길이를 뺀 값에 대해 다시 확인

import sys
input = sys.stdin.readline

N = int(input())


def solve(N, dp=[3]):
    if N <= 3:
        if N == 1:
            return "m"
        else:
            return "o"

    count = 1
    while dp[-1] < N:
        mid = 1 + (count+2)
        dp.append(dp[-1]*2 + mid)
        count += 1
    l = dp[-2]
    if N - l == 1:
        return "m"
    elif N - l <= mid:
        return "o"
    else:
        dp.clear()
        dp.append(3)
        return solve(N-l-mid)


print(solve(N))
