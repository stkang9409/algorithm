# 숫자 나오면 숫자 스택에 넣기
# 더하기 나오면 결과 정수에 숫자 스택 더하기
# 빼기 나오면 빼기 작업대에 넣기


import sys
input = sys.stdin.readline


def solve():
    prob = input().rstrip()

    opt = prob.split("-")

    for i in range(len(opt)):
        opt[i] = sum(map(int, opt[i].split("+")))

    result = opt[0]
    for i in range(1, len(opt)):
        result -= opt[i]

    print(result)


solve()
