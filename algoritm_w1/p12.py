n = int(input())

for _ in range(n):
    s = list(input())
    s[0] = 1 if s[0] == "O" else "X"
    retval = 1 if s[0] == 1 else 0
    for i in range(1, len(s)):
        before = s[i-1]
        if s[i] == "O" and before != "X":
            s[i] = before + 1
            retval += s[i]
        elif s[i] == "O" and before == "X":
            s[i] = 1
            retval += 1

    print(retval)
