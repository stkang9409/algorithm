import sys

sys.setrecursionlimit(10**6)


def init(idx, left, right):
    if left == right:
        segtree[idx] = [left, h[left]]
        return segtree[idx]
    tmp1 = init(2*idx+1, left, (left+right)//2)
    tmp2 = init(2*idx+2, (left+right)//2 + 1, right)
    if tmp1[1] < tmp2[1]:
        segtree[idx] = tmp1
        return tmp1
    segtree[idx] = tmp2
    return tmp2


def minq(idx, l, r, left, right):
    if left <= l and r <= right:
        return segtree[idx]
    if r < left or right < l:
        return [None, 10**9+1]
    tmp1 = minq(2*idx+1, l, (l+r)//2, left, right)
    tmp2 = minq(2*idx+2, (l+r)//2 + 1, r, left, right)
    if tmp1[1] < tmp2[1]:
        return tmp1
    return tmp2


def histmax(left, right):
    if left > right:
        return 0
    tmp = minq(0, 0, n-1, left, right)
    midx = tmp[0]
    return max(tmp[1]*(right-left+1), histmax(left, midx-1), histmax(midx+1, right))


h = [int(sys.stdin.readline().split()[0])
     for _ in range(int(sys.stdin.readline().split()[0]))]
n = len(h)
segtree = [None]*(10*n-1)
init(0, 0, n-1)
print(histmax(0, n-1))
