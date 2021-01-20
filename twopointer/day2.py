import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    lis = [list(map(int, input().split())) for _ in range(N)]
    check = [N-1]*N

    for c in range(N):
        max_index = 0
        for i in range(N):
            max_index = max(i, max_index, key=lambda x: lis[check[x]][x])
        if c == N-1:
            print(lis[check[max_index]][max_index])
        check[max_index] -= 1


solve()
