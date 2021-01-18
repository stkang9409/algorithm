# 동전 가지고 K 만들기
# 동전은 오름차 순으로 주어진다.

# 큰 것부터 넣기 (A(i)가 A(i-1)의 배수이기 떄문에 그리디 가능)


import sys
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    nums = [0]*N

    for i in range(N):
        nums[i] = int(input())

    count = 0
    remain = K
    while nums or remain > 0:
        num = nums.pop()
        count += remain//num
        remain -= remain//num * num

    print(count)


solve()
