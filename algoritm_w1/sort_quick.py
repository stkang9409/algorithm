A = list(map(int, input().split()))


def partial(arr, start, end):
    j, p = start, end
    for i in range(start, end):
        if arr[i] < arr[end]:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[end] = arr[end], arr[j]
    p = j
    return p


def quick(A, start=0, end=len(A)-1):
    if start < end:
        q = partial(A, start, end)  # 피봇값의 인덱스
        quick(A, start, q-1)  # 피봇값 좌
        quick(A, q+1, end)  # 피봇값 우

    return A


print(quick(A))
