N = int(input())
sticks = reversed([int(input()) for i in range(N)])

stack = []

for stick in sticks:
    if not len(stack):
        stack.append(stick)
        continue

    if stack[-1] < stick:
        stack.append(stick)

print(len(stack))
