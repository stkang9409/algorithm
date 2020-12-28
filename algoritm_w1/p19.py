a, b = map(int, input().split())

r_a = a//100 + (a - a//100*100 - a % 10) + a % 10 * 100
r_b = b//100 + (b - b//100*100 - b % 10) + b % 10 * 100

print(max(r_a, r_b))


# a, b = map(str, input().split())

# a = a[::-1]
# b = b[::-1]

# print(max(a, b))
