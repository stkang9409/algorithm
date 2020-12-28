x, y, w, h = map(int, input().split())

left = x
right = w-x
down = y
up = h-y

print(min(left, right, down, up))
