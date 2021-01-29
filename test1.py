import sys

input = sys.stdin.readline

def solve():
    N, d, k, c = map(int, input().split())
    sushi = [int(input()) for i in range(N)]

    gotten = {c: 1}

    for i in range(N-1, N-k-1, -1):
        if gotten.get(sushi[i]):
            gotten[sushi[i]] += 1
        else:
            gotten[sushi[i]] = 1
    
    result = len(gotten)

    for i in range(N-1, -1, -1):
        gotten[sushi[i]] -= 1

        if gotten[sushi[i]] == 0:
            del gotten[sushi[i]]

        if gotten.get(sushi[i-k]):
            gotten[sushi[i-k]] += 1
        else:
            gotten[sushi[i-k]] = 1

        
        result = max(result, len(gotten))

    print(result)
    return

solve()

    
    