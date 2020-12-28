import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

que = deque(range(1, N+1))

while que:
    x = que.popleft()
    if que:
        x = que.popleft()
        que.append(x)

print(x)
