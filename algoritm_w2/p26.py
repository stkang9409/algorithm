import sys
from heapq import heappush, heappop
input = sys.stdin.readline
heap = []

N = int(input())

for _ in range(N):
    heappush(heap, int(input()))

result = 0
while len(heap) != 1:
    a = heappop(heap)
    b = heappop(heap)
    result += a+b
    heappush(heap, a+b)

print(result)
