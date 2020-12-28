a = input()
b = input()
ret_x, ret_l = 0, 1
s = min(a, b)
big = max(a, b)
for x in range(len(big)):
    i, l = 0, ret_l
    while i+l < len(s) and x+l < len(big):
        if s[i] == big[x] and s[i+l] == big[x+l] and s[i:i+l] == big[x:x+l]:
            l += 1
            working = s[i:i+l]
        else:
            i += 1
        if ret_l < l:
            ret_l = l
            ret_x = x

print(ret_l)
print(big[ret_x: ret_x+ret_l])
