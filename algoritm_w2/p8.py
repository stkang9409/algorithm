a, b, c = map(int, input().split())


def power(a, b, c):
    if b < 10:
        return a**b % c

    if b % 2 == 0:
        result = power(a, b//2, c)**2 % c
    else:
        result = (power(a, b//2, c)**2 % c * a % c) % c

    return result


print(power(a, b, c))
