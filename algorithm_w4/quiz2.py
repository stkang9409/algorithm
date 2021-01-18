import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solve():
    R, C = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(R)]
    cmd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # dp는 -1로 초기화 visited와 dp의 기능을 동시에 수행한다.
    dp = [[-1]*C for _ in range(R)]
    # 내가 도달해야하는 위치를 1로 초기화해서, 도착지점에 도달했다는 사실을 컴퓨터가 알아차릴 수 있도록 해준다.
    # dp[i][j]의 의미: i,j로부터 도착지점까지 갈 수 있는 경로의 수
    dp[-1][-1] = 1

    def dfs(i, j):
        # 내가 지나간 적 있는 경로면, 이 지점에서 도착지점까지 갈 수 있는 경로가 몇개나 되는지를 반환해준다
        if dp[i][j] != -1:
            return dp[i][j]

        # 0으로 초기화의 의미: 내가 i,j를 한번 들렀다. 아직 여기가 도착 가능한 경로 상에 있는지는 나도 모른다.
        dp[i][j] = 0
        # 네가지 방향으로 한번 가보자.
        for di, dj in cmd:
            ni, nj = i+di, j+dj
            # 가려는 방향이 길일 때만 간다. 넘어갈 수는 없다.
            if 0 <= ni < R and 0 <= nj < C:
                # 내리막길일때만 갈 수가 있다.
                if graph[i][j] > graph[ni][nj]:
                    # ni,nj로 가니까 n가지 방법으로 도착이 가능하더라, 그러니까 일단 n을 저장하고, 남은 세방향도 확인해보자.
                    dp[i][j] += dfs(ni, nj)

        # 이 지점에서 도착지점까지 갈 수 있는 경로가 몇개나 되는지 저장해둔걸 반환해준다
        return dp[i][j]

    print(dfs(0, 0))


solve()
