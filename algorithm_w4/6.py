import sys
input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(1 << N) for _ in range(N)]


def recur(cur, visited):
    if visited == (1 << N)-1:
        return table[cur][0] or float('inf')

    if dp[cur][visited]:
        return dp[cur][visited]

    result = float("inf")
    for i in range(N):
        if not visited & (1 << i) and table[cur][i]:
            result = min(result, recur(
                i, (visited | (1 << i))) + table[cur][i])

    dp[cur][visited] = result
    return result


ans = min(float("inf"), recur(0, 1))
print(ans)
