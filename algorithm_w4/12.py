# 나중에 쓰는 것을 먼저 뺀다.


import sys
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    multitap = set()
    distance = [[float('inf')] for _ in range(K+1)]

    for i in range(K-1, -1, -1):
        distance[sequence[i]].append(i)

    count = 0
    i = 0

    # 멀티탭이 꽉차면 끝남
    while count < N and i < K:
        if sequence[i] not in multitap:
            multitap.add(sequence[i])
            distance[sequence[i]].pop()
            count += 1
        else:
            distance[sequence[i]].pop()
        i += 1
    count = 0

    # 멀티탭 꽉차있을때
    for i in range(i, K):
        if sequence[i] not in multitap:
            # 제일 늦게 쓰는 전기용품
            noneed = list(multitap)[0]
            for x in multitap:
                noneed = max(noneed, x, key=lambda y: distance[y][-1]-i)
            multitap.remove(noneed)
            count += 1
            multitap.add(sequence[i])
            distance[sequence[i]].pop()
        else:
            distance[sequence[i]].pop()

    print(count)


solve()
