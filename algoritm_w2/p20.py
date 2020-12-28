from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
que = deque([])

for _ in range(N):
    cmd = input().rstrip().split()

    if cmd[0] == "push":
        que.append(cmd[1])
    elif cmd[0] == "pop":
        result = que.popleft() if que else -1
        print(result)
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        result = 0 if que else 1
        print(result)
    elif cmd[00] == "front":
        result = que[0] if que else -1
        print(result)
    else:
        result = que[-1] if que else -1
        print(result)
