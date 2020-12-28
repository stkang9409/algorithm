retval = [0, 0]
for i in range(9):
    a = int(input())
    if a > retval[0]:
        retval[0], retval[1] = a, i

print(retval[0])
print(retval[1]+1)
