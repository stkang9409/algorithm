import sys
input = sys.stdin.readline


def solve():
    target = input().rstrip()
    word = input().rstrip()

    l = len(word)
    i = 0
    count = 0
    while i < len(target)-l+1:
        if target[i:i+l] == word:
            i += l
            count += 1
            continue
        i += 1

    return count


print(solve())
