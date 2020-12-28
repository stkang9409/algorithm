N = int(input())


def cycle(n, count=0, target=N):
    a = n // 10
    b = n % 10
    c = (a + b) % 10 + b*10
    if c == target:
        print(count + 1)
        return
    else:
        count += 1
        cycle(c, count)


cycle(N)
