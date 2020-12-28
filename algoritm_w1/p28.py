N = int(input())

set_point = [0] * N
flag = [True] * N
flag_b = [True] * (2*N - 1)
flag_c = [True] * (2*N - 1)


def put(n, count=0):
    if n == -1:
        count += 1
    else:
        for i in range(N):
            if flag[i] and flag_b[n+i] and flag_c[n-i+N-1]:
                set_point[n] = i
                flag[i] = flag_b[i+n] = flag_c[n-i+N-1] = False
                count = put(n-1, count)
                flag[i] = flag_b[i+n] = flag_c[n-i+N-1] = True

    return count


print(put(N-1))
