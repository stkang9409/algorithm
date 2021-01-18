import sys
input = sys.stdin.readline

N = int(input())
eN = int(input())
events = [list(map(int, input().split())) for _ in range(eN)]
events = [0] + events
solved = [0]*(eN+1)
dp = [[0]*(eN+1) for _ in range(eN+1)]


def distance(coord1, coord2):
    i, j = coord1
    x, y = coord2
    return abs(i-x) + abs(j-y)


def dfs(step):
    if step == 1:
        dp[step][0] = distance((0, 0), events[step])
        dp[0][step] = distance((N, N), events[step])
        return min(dp[step][0], dp[0][step])

    for i in range(step):
        if not dp[step][i]:
            dp[step][i] = min(dp[step][i], dfs(step-1) +
                              distance(events[step], events[step-1]))
        if not dp[i][step]:
            dp[i][step] = min(dp[i][step], dfs(step-1) +
                              distance(events[step], events[step-1]))

    return min(dp[i][step], dp[step][i])


print(dfs(eN))
