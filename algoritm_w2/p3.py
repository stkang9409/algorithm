import sys

input = sys.stdin.readline

house_num, router_num = map(int, input().split())
coords = [int(input()) for _ in range(house_num)]
coords.sort()


def check(distance, coords=coords):
    count = 1  # 여기서 0으로 해놓아서 틀림
    router_pos = coords[0]

    for coord in coords:
        distance_from_router = coord - router_pos

        if distance_from_router >= distance:
            router_pos = coord
            count += 1

    return count


def search_distance(start=1, end=coords[-1]-coords[0], router_num=router_num):

    while start <= end:
        middle = (start+end)//2

        if check(middle) >= router_num:
            result = middle
            start = middle + 1
        else:
            end = middle - 1

    return result


print(search_distance())
