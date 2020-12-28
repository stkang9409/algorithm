"""

    1. 모든 루트에 대하여 parent, cl = parent * 2, cr = parent * 2 + 1 (이진은 곱하기 가능)
    2. 비교
    3. 이동

    1. 최대힙의 특성: A[parent(i)] >= A[i] 부모가 자식보다 크거나 같다.

"""

N = int(input())
arr = [int(input()) for i in range(N)]


def heap(arr, i, heapsize):
    l = i*2
    r = i*2+1
    largest = i

    if l <= heapsize and r <= heapsize:
        largest = max(i, l, r, key=lambda x: arr[x])

    if largest != i:  # 내려가기
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, largest, heapsize)


for i in range(N+1, -1, -1):
    heap(arr, i, len(arr)-1)


for i in range(N - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heap(arr, 0, i-1)

print(arr)
