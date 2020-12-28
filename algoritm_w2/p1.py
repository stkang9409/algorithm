N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()  # 정렬 안하면 이진 탐색 안되는거 기억해야함


def search(x):
    start = 0
    end = len(A) - 1

    while start <= end:
        middle = (start+end)//2
        if A[middle] == x:
            return 1
        elif A[middle] < x:
            start = middle + 1
        else:
            end = middle - 1
    return 0


for x in arr:
    print(search(x))
