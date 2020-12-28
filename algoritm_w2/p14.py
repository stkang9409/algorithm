def check(arr):
    stack = []
    for c in arr:
        if c == "(":
            stack.append(1)
        elif len(stack):
            stack.pop()
        else:
            print("NO")
            return

    if len(stack):
        print("NO")
    else:
        print("YES")
    return


N = int(input())
for _ in range(N):
    arr = input()
    check(arr)
