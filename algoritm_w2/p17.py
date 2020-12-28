import sys
input = sys.stdin.readline

N = int(input())

circles = [list(map(int, input().split())) for _ in range(N)]


def change_to_coord(circles):
    coords = [0]*(N*2)
    for i in range(len(circles)):
        circle = circles[i]
        open_coord = circle[0] - circle[1]
        close_coord = circle[0] + circle[1]
        coords[i] = [open_coord, "o"]
        coords[-1-i] = [close_coord, "c"]

    coords.sort(key=lambda x: (x[0], x[1]))
    return coords


def solve(circles):
    count = 0
    coords = change_to_coord(circles)
    stack = []
    for coord in coords:
        if not stack:
            stack.append(coord)
            continue
        if coord[1] == "c":
            val = stack.pop()
            in_circle_radius = 0

            while stack and isinstance(val, int):
                in_circle_radius += val
                val = stack.pop()

            radius = coord[0] - val[0]

            if in_circle_radius == radius:
                count += 1

            stack.append(radius)
        else:
            stack.append(coord)

    print(count + N + 1)


solve(circles)
