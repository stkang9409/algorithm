import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

for _ in range(M+K):
    t, *info = map(int, input().split())
