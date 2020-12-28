N = int(input())
arr = [int(input()) for _ in range(N)]


def radix(arr, exp):
    count = [0]*10
    result = [0]*N

    for n in arr:
        count[n//exp % 10] += 1

    for i in range(1, N):
        count[i] += count[i-1]

    for i in range(N-1, -1, -1):
        result[count[arr[i]//exp % 10]-1] = arr[i]
        count[arr[i]//exp % 10] -= 1

    arr = result[:]
    return arr


m_val = max(arr)

exp = 1
while m_val // exp != 0:
    arr = radix(arr, exp)
    exp *= 10

print(arr)
