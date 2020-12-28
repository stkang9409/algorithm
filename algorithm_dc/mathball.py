N, M = map(int, input().split())
X = [int(i) for i in input().split()]


def isPossible(k):
    cnt, S = 1, 0
    for x in X:
        if S+x > k:
            cnt += 1
            S = x
        else:
            S += x
    if cnt > M:
        return False
    return True


l = max(X)
r = sum(X)

while l < r:
    m = (l + r) // 2
    if isPossible(m):
        r = m
    else:
        l = m+1
print(r)

div, cnt, S = 1, 0, 0  # S = sum, cnt = div안 개수 div=나눠진 구역

for i in range(0, N):
    if M-div == N-i or S+X[i] > r:  # 합이 최대값을 넘어가거나, 남은 만들어야하는 구역 개수 가 남은 원소 개수일때
        print(cnt, end=' ')
        S = X[i]
        cnt = 1
        div += 1
    else:
        S += X[i]
        cnt += 1
print(cnt)
