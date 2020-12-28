N = int(input())


def move(n, start=1, end=3, middle=2):
    if n == 1:
        print(f"{start} {end}")
    else:
        move(n-1, start, middle, end)
        move(1, start, end, middle)
        move(n-1, middle, end, start)


print(str(2**N-1))
if N <= 20:
    move(N)
