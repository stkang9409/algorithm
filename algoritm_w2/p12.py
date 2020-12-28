import sys

input = sys.stdin.readline

arr = []


def push(arr, x):
    arr.append(x)


def size(arr):
    print(len(arr))


def empty(arr):
    if len(arr):
        print(0)
    else:
        print(1)


def top(arr):
    if len(arr):
        print(arr[-1])
    else:
        print(-1)


def pop(arr):
    if len(arr):
        print(arr.pop())
    else:
        print("-1")


N = int(input())
for _ in range(N):
    command = list(map(str, input().split()))

    if command[0] == "push":
        arr.append(int(command[1]))
    elif command[0] == "top":
        top(arr)
    elif command[0] == "size":
        size(arr)
    elif command[0] == "empty":
        empty(arr)
    else:
        pop(arr)
