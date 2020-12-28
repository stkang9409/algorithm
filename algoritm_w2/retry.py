# 트리 만들기
# return [최소값 인덱스, ]


def init(idx, start, end):
    if start == end:
        segtree[idx] = [start, h[start]]
        return segtree[idx]

    mid = (start+end)//2
    cl = 2*idx+1
    cr = 2*idx+2

    left_part = init(cl, start, mid)
    right_part = init(cr, mid+1, end)
    # 좌 우 중 더 작은 값 트리에 넣고 반환
    if left_part[1] < right_part[1]:
        segtree[idx] = left_part
        return left_part
    segtree[idx] = right_part
    return right_part


# l,r은 히스토그램 왼쪽 오른쪽
def minq(idx, l, r, start, end):
    if start <= l and r <= end:
        return segtree[idx]
    if r < start or end < l:
        return [None, 10**9+1]

    mid = (l+r)//2
    left_part = minq(2*idx+1, l, mid, start, end)
    right_part = minq(2*idx+2, mid + 1, r, start, end)
    if left_part[1] < right_part[1]:
        return left_part
    return right_part


def histmax(left, right):
    if left > right:
        return 0
    min_height_info = minq(0, 0, N-1, left, right)
    min_height_index = min_height_info[0]
    min_height = min_height_info[1]
    return max(min_height*(right-left+1), histmax(left, min_height_index-1), histmax(min_height_index+1, right))


N = int(input())
h = [int(input()) for _ in range(N)]
segtree = [None]*(N**4)
init(0, 0, N-1)
