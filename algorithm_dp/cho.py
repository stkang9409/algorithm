# 원타곤 습격
# 두개의 원 1~16 배열 두개로 나타낼 수 있음.
# w는 특수소대원 사람 수, 특수 소대원 수 다 똑같음
# 구역 별 적이 입력으로 들어온다
# 한 특수소대 최대 두 구역 커버 가능
# 구역 적의 합은 특수 소대원 수 W보다 작거나 같아야함

# 입력: T, N(구역 갯수), W(소대원 수)

import sys
input = sys.stdin.readline
T = int(input())


def dfs(used):
    if len(visited) == 0:
        dp[used] = 0
        return dp[used]

    if dp.get(used):
        return dp[used]

    for i in range(l):
        if not used & (1 << i) and candidate[i][0] in visited and candidate[i][1] in visited:
            visited.remove(candidate[i][0])
            visited.remove(candidate[i][1])
            print(candidate[i], dp.get(used, 0))
            dp[used] = max(dp.get(used, 0), dfs(used | (1 << i)) + 1)
            visited.add(candidate[i][0])
            visited.add(candidate[i][1])
    return dp.get(used, 0)


for _ in range(T):
    N, W = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(2)]
    candidate = set()
    visited = set()
    for i in range(2):
        for j in range(N):
            if area[i][j] + area[i][j-1] <= W:
                candidate.add(((i, j), (i, j-1)))
                visited.add((i, j))
                visited.add((i, j-1))

            if j+1 < N:
                if area[i][j] + area[i][j+1] <= W:
                    candidate.add(((i, j), (i, j+1)))
                    visited.add((i, j))
                    visited.add((i, j+1))

            if i == 1 and area[i][j] + area[i-1][j] <= W:
                candidate.add(((i, j), (i-1, j)))
                visited.add((i, j))
                visited.add((i-1, j))

    candidate = list(candidate)
    l = len(candidate)
    dp = {}
    result = 0
    for i in range(l):
        visited.remove(candidate[i][0])
        visited.remove(candidate[i][1])
        result = max(result, dfs(1 << i)+1)
        visited.add(candidate[i][0])
        visited.add(candidate[i][1])

    print(2*N - result)
