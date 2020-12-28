N = int(input())

a = [0]
b = [0]
c = [0]


def nqueen(pos=0, n=N, count=[0]):
    if pos == (1 << N) - 1:
        count[0] += 1
    else:
        for i in range(N):
            if not (a[0] & (1 << i)) and not (b[0] & (1 << (n - i + N - 1))) and not (c[0] & (1 << (i + n))):
                a[0] = a[0] | (1 << i)
                b[0] = b[0] | (1 << (n - i + N-1))
                c[0] = c[0] | (1 << (i + n))
                pos = pos | (1 << n-1)
                nqueen(pos, n-1)
                a[0] = a[0] & ~(1 << i)
                b[0] = b[0] & ~(1 << (n - i + N-1))
                c[0] = c[0] & ~(1 << (i + n))

    return count[0]


print(nqueen())
