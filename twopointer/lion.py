"""
# 문제
# 꿀귀 라이언 인형과, 마찬가지로 꿀귀인 어피치 인형이 N개 일렬로 놓여 있다. 
# 라이언 인형은 1, 어피치 인형은 2로 표현하자. 
# 라이언 인형이 K개 이상 있는 가장 작은 연속된 인형들의 집합의 크기를 구하여라.

# 입력
# 첫 줄에 N과 K가 주어진다. (1 ≤ K ≤ N ≤ 106)

# 둘째 줄에 N개의 인형의 정보가 주어진다. (1 또는 2)

# 출력
# K개 이상의 라이언 인형을 포함하는 가장 작은 연속된 인형들의 집합의 크기를 출력한다. 
# 그런 집합이 없다면 -1을 출력한다.
"""
import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())

    kfs = list(map(int, input().split()))
    ans = float('inf')
    lion = 0

    s, e = 0, 0

    while s <= e:
        print("rnasdf", lion)

        if lion < K:
            if 
            if kfs[e] == 1:
                lion += 1
            e += 1
        else:
            print(ans)
            ans = min(ans, e-s)
            if kfs[s] == 1:
                print("씨발")
                lion -= 1
            s += 1
        
    print(ans)

solve()
    