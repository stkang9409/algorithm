import sys
input = sys.stdin.readline

heap = ["x"]


def push(x):
    heap.append(x)
    child = len(heap)-1
    parent = child//2

    while parent != 0 and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child//2


def pop():
    heap[-1], heap[1] = heap[1], heap[-1]
    result = heap.pop()
    print(result)

    parent = 1
    cl = parent*2
    cr = parent*2 + 1
    while cl < len(heap) or cr < len(heap):
        cl = parent*2
        cr = parent*2 + 1
        largest = parent

        if cl < len(heap) and heap[cl] > heap[largest]:
            largest = cl
        if cr < len(heap) and heap[cr] > heap[largest]:
            largest = cr

        if parent != largest:
            heap[parent], heap[largest] = heap[largest], heap[parent]
            parent = largest
        else:
            break


N = int(input())

for _ in range(N):
    cmd = int(input())

    if cmd == 0:
        if len(heap) != 1:
            pop()
        else:
            print(0)
    else:
        push(cmd)
