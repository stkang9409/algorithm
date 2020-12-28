n = int(input())

for _ in range(n):
    s = list(map(int, input().split(' ')))
    l = s[0]

    # 평균 구하기

    average = sum(s[1:])/l

    # 평균 이상 학생 구하기
    n = 0
    for x in s[1:]:
        if x > average:
            n += 1

    retval = (round(n/l, 5) * 100)
    print("%.3f" % retval+"%")
