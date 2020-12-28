check = [True] * 10001
check[0], check[1] = False, False

for n in range(2, 10001):
    if check[n]:
        i = n*2
        while i < len(check):
            check[i] = False
            i += n

T = int(input())

for _ in range(T):
    n = int(input())
    divided = int(n/2)
    if check[divided]:
        print(divided, divided)
    else:
        s = divided - 1
        b = divided + 1
        while True:
            if check[s] and check[b]:
                print(s, b)
                break
            else:
                s -= 1
                b += 1
