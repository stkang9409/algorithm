"""
# 철로

기본적인 풀이:
1. 모든 x를 방문하면서 선로가 포함하는 통근길의 합을 구한다.
2. 통근길 합의 최댓값을 같는 x를 출력

문제점:
1. 시간 초과

해결책:
1. 통근길 합을 우선순위 큐에 저장
2. 한 방에 출력

풀이 순서:
1. 통근길 x로 정렬 O(nlogn)
2. 각 x 마다
    - path = (x, x+선로거리)
    - path 안의 통근길 갯수 합: 통근길(x1,x2) ( 후보군 줄이기: x1 이 x+선로거리보다 크거나 x보다 작으면 제거)
    - 다 확인해서 total에 더하기
    - PriorityQueue에 넣기
3. que.get() 출력

"""

import sys
from queue import PriorityQueue
input = sys.stdin.readline

que = PriorityQueue()
route_num = int(input())
routes = sorted([sorted(list(map(int, input().split())))
                 for _ in range(route_num)], key=lambda x: x[0])
path_len = int(input())
xs = [route[0] for route in routes]
xs = list(set(xs))


def count(path, route):
    if path[0] <= route[0] and route[1] <= path[1]:
        return 1
    return 0


def solve(path_len):
    max_val = 0
    for x in xs:
        result = 0
        path = [x, x+path_len]
        for route in routes:
            result += count(path, route)
        max_val = max(max_val, result)
    return max_val


print(solve(path_len))
