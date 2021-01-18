import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    gems = [list(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]
    gems.sort(key=lambda x: x[0])
    bags.sort()

    candidate = []
    i = 0
    total = 0
    for bag in bags:
        # 작은 가방보다 작으면 전부 힙에 넣는다.
        while i < N and bag >= gems[i][0]:
            heappush(candidate, -gems[i][1])
            i += 1
        # 그중 가치가 가장 큰 친구를 빼서 더한다.
        if candidate:
            total += heappop(candidate)

    print(-total)


solve()
# 가치가 제일 큰걸 제일 작은 가방에 넣는다
# 같은 가치면 최대한 큰걸 넣는다
# 가방 작은 순으로 정렬
