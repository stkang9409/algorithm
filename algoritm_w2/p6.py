import sys
input = sys.stdin.readline

hunter_num, animal_num, L = map(int, input().split())
hunters = sorted(list(map(int, input().split())))
animals = [list(map(int, input().split())) for _ in range(animal_num)]


def get_distance(animal, hunter_i):
    result = abs(animal[0] - hunters[hunter_i]) + animal[1]
    return result


def count_huntable():
    count = 0

    for animal in animals:
        pl = 0
        pr = hunter_num - 1

        while pl <= pr:
            pc = (pl+pr)//2

            if hunters[pc] == animal[0]:
                break
            elif hunters[pc] < animal[0]:
                pl = pc + 1
            else:
                pr = pc - 1

        result = min(get_distance(animal, pc), get_distance(
            animal, pl), get_distance(animal, pr))

        if result <= L:
            count += 1

    print(count)


count_huntable()
