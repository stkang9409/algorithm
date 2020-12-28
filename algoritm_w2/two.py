import sys


def distance(p1, p2):
    return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])


# lists는 x축 기준으로 정렬되어 있음.
def solve(start, end, lists):

    if start == end:
        return float('inf')

    if end - start < 2:
        return distance(lists[start], lists[end])

    mid = int((start + end) / 2)
    d = min(solve(start, mid, lists), solve(mid+1, end, lists))
    # print(str(start), " -> " , str(end))
    # print("\td = ", str(d))
    # 중앙선 기준으로 x좌표의 거리가 d를 넘는건 후보군에서 제외
    candidate = []
    for i in range(start, end+1):
        dx = lists[i][0] - lists[mid][0]

        if dx * dx < d:
            candidate.append(lists[i])

    # 후보군을 y축 기준으로 정렬
    candidate = sorted(candidate, key=lambda x: x[1])

    # 한쪽으로 쓸면서 최솟값 갱신
    for i in range(0, len(candidate)-1):
        for j in range(i+1, len(candidate)):
            dy = candidate[i][1] - candidate[j][1]

            if dy * dy < d:
                d = min(d, distance(candidate[i], candidate[j]))
            else:
                break

    return d


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    N = int(input())

    lists = []
    for i in range(N):
        lis = list(map(int, sys.stdin.readline().rstrip().split()))
        lists.append(lis)

    # x축을 기준으로 정렬
    lists = sorted(lists, key=lambda x: x[0])
    print(solve(0, N-1, lists))
