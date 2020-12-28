def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    while len(arr1) > i and len(arr2) > j:
        if arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1

    if i == len(arr1):
        result = result + arr2[j:]
    else:
        result = result + arr1[i:]

    return result


def sorting(arr):
    l = len(arr)
    if l <= 1:
        return arr
    else:
        return merge(sorting(arr[:l//2]), sorting(arr[l//2:]))


N = int(input())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)

results = sorting(arr)

for result in results:
    print(result)
