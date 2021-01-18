# 서류성적과 면접성적이 둘 중 하나는 최고여야한다.
# 서류 성적에 대해 정렬 서류 성적 1등은 무조건 합격
# 서류 성적 2등인 친구는 1등에 비해 면접 성적이 높아야한다.
# 면접성적이 더 낮으면 탈락, 더 높으면 면접성적에 대해서 현재 합격자 중 1등이 된다.
# 서류 성적 3등인 친구는 2등에 비해 면접 성적이 높아야한다.
# 즉 현재까지 면접 성적 1등보다 면접 성적이 높아야한다.

# 서류 및 면접 성적 배열 선언
# 합격자 카운트
# 최후 합격자 면접 성적(커트라인)
# 서류 성적 순으로 반복문을 돌리며 해당 지원자가 커트라인을 넘기면(등수가 더 낮으면) 카운트 더하기 일, 커트라인 갱신, 아니면 그냥 넘어가기
import sys
input = sys.stdin.readline


def solve():
    N = int(input())

    scores = {}

    for _ in range(N):
        paper, interview = map(int, input().split())
        scores[paper] = interview

    cutline = scores[1]
    count = 1
    for i in range(2, N+1):
        if scores[i] < cutline:  # 등수가 낮아야 더 좋은 것
            count += 1
            cutline = scores[i]

    print(count)


for _ in range(int(input())):
    solve()
