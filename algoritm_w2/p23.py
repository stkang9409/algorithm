import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
apple_num = int(input())
apple_coords = [list(map(int, input().split())) for _ in range(apple_num)]
move_num = int(input())
moves = [list(map(str, input().split())) for _ in range(move_num)]
moves.reverse()
dic = {"D": 1, "L": -1}


def count_time(N):
    count = 0
    snake = deque([[1, 1], ])
    lr = 1
    ud = 0
    while snake:
        head = snake[-1][:]
        if lr:
            head[1] += lr
        else:
            head[0] += ud

        count += 1

        if head in snake or head[0] < 1 or N < head[0] or head[1] < 1 or N < head[1]:
            break

        snake.append(head)
        if head not in apple_coords:
            snake.popleft()
        else:
            apple_coords.remove(head)

        if moves and count == int(moves[-1][0]):
            if lr:
                ud = lr * dic[moves[-1][1]]
                lr = 0
            else:
                lr = ud * -dic[moves[-1][1]]
                ud = 0
            moves.pop()

    return count


print(count_time(N))
