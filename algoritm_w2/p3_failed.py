import sys
sys.setrecursionlimit(50000)
N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
distances = [0] * N


def bin_search(arr, start, end, C_num):
    if C_num == 1:
        print(start, end)
        return arr[end-1] - arr[start]

    pl = start
    pr = end - 1

    max_distance = (arr[end-1]-arr[start])//(C_num) + start
    ans = float('inf')
    while True:
        pc = (pl + pr)//2
        if arr[pc] == max_distance:
            ans = min(arr[pc] - arr[start],
                      bin_search(arr, pc, end, C_num-1))
            break
        elif arr[pc] < max_distance:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            if arr[pl] - max_distance >= max_distance - arr[pr]:
                ans = min(arr[pr] - arr[start],
                          bin_search(arr, pr, end, C_num-1))
            else:
                ans = min(arr[pl] - arr[start],
                          bin_search(arr, pl, end, C_num-1))
            break

    return ans


for i in range(1, N):
    distances[i] = arr[i] - arr[0]

distances.sort()
print(bin_search(distances, 0, N, C-1))
