# 도수정렬
import sys
RANGE = 10001

N = int(sys.stdin.readline())
working = [0] * RANGE
for i in range(N):
    a = int(sys.stdin.readline())
    working[a] = working[a] + 1

for i in range(RANGE):
    if working[i] != 0:
        for _ in range(working[i]):
            print(i)
