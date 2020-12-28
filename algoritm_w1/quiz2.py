N = int(input())
in_arr = [int(input()) for _ in range(N)]
arr = [1] * N
result = []


def sum(arr, clone, count=0):
    if len(arr) <= 1:
        return 0
    for i in range(len(arr)-1):
        tmp = arr[i]
        tmp_arr = arr[:i] + arr[i+1:]
        if tmp_arr[i] + tmp < 4:
            tmp_arr[i] += tmp
            if tmp_arr not in clone:
                clone.append(tmp_arr)
                count = sum(tmp_arr, clone, count) + 1

    return count


for i in in_arr:
    clone = []
    arr = [1] * i
    print(sum(arr, clone)+1)
    clone.clear()
