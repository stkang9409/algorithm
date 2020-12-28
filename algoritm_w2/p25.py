from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
min_heap = []
max_heap = []

for _ in range(N):
    n = int(input())

    if len(max_heap) - len(min_heap) > 0:
        heappush(min_heap, n)
    else:
        heappush(max_heap, -n)

    if min_heap and -max_heap[0] > min_heap[0]:
        heappush(max_heap, -heappop(min_heap))
        heappush(min_heap, -heappop(max_heap))

    print(-max_heap[0])
