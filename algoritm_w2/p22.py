from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
result = []
que = deque(range(1, N+1))

while que:
    for _ in range(1, K):
        que.append(que.popleft())
    result.append(que.popleft())

print('<' + ", ".join(map(str, result)) + '>')
