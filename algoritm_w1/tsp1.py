import sys
input = sys.stdin.readline

n = int(input())
adj = [list(map(int, input().split())) for i in range(n)]
cpl = (1 << n)-1  # 순회완료 상태 비트마스크
INF = 1 << 30  # 큰 값


def solve(cur, visited):
    if visited == cpl:  # 순회가 끝나면
        return adj[cur][start] or INF  # 원래 지점으로 돌아가기 혹은(0이면) 무한대 반환

    if DP[cur][visited]:
        return DP[cur][visited]  # 같은 상태였던 적이 있으면 최소값으로

    ans = INF

    for i in range(n):
        # cur에서 i로 갈 수 있고, 방문한 적이 없으면
        if adj[cur][i] and not visited & (1 << i):
            # 모든 노드를 탐색하며 최솟값만 저장
            ans = min(ans, solve(i, visited | (1 << i))+adj[cur][i])
    DP[cur][visited] = ans  # 지금부터 문제 종료까지의 최적 해를 저장
    return ans


ans = INF
start = 0
DP = [[0]*(1 << n) for _ in range(n)]
ans = min(ans, solve(start, 1 << start))  # 순회 불가능할 때 대비
print(ans)
