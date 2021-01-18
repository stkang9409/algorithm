from bisect import bisect as bs
K = int(input())

dp = [1, 2]
# dp[i] = 2의 거듭 제곱이 되는 i번째 수가 몇번 째에 나오는가

ans = 0
# 출력 할 2진수 형태의 값

while dp[-1]+dp[-2] <= K:
    dp.append(dp[-1]+dp[-2])
# K보다 작은 2의 거듭 제곱 꼴을 모두 찾는다.


while K:
    i = bs(dp, K)-1
    # K가 DP의 몇번째 원소에 들어갈 수 있을 지 찾아서 i에 저장

    ans += 10**i
    # K 보다 작은 가장 큰 2의 거듭제곱을 만드는데 걸리는 횟수를 K에서 제거한다
    # 1 << i == 10**n
    K -= dp[i]

print(ans)
