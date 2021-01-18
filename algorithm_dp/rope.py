import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    ropes = [int(input()) for _ in range(N)]
    ropes.sort()

    result = 0
    for i in range(N):
        result = max(result, ropes[i]*(N-i))

    print(result)


solve()
