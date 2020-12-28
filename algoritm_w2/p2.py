import sys

input = sys.stdin.readline

tree_num, need = map(int, input().split())
trees = list(map(int, input().split()))


def get_tree_amount(h):
    amount = 0
    for tree in trees:
        amount += tree - h if tree - h > 0 else 0
    return amount


def bin_search(need):
    low = 0
    high = max(trees)
    result = 0

    while low <= high:
        middle = (low + high)//2

        if get_tree_amount(middle) >= need:
            result = middle
            low = middle + 1
        else:
            high = middle - 1

    return result


print(bin_search(need))
