n = int(input())

for _ in range(n):
    x, s = map(str, input().split())
    retval = ""
    for c in s:
        retval += c*int(x)
    print(retval)
