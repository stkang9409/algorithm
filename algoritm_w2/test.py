import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

N, idx = map(int, input().split())
nums = list(map(int, input().split()))
heap = nums[:]
max_heap = [-i for i in nums]
heapify(max_heap)
heapify(heap)
count = 0
flag = {}

while count < idx:
    a = heappop(heap)
    for num in nums:
        if len(max_heap) > idx and a*num > -max_heap[0]:
            continue
        if not flag.get(a*num):
            heappush(heap, a*num)
            heappush(max_heap, -a*num)
            flag[a*num] = True
    count += 1


print(a)
