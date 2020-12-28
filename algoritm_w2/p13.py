N = int(input())
count = 0
stack = []
for _ in range(N):
    i = int(input())
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))
