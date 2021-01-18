import sys
input = sys.stdin.readline


def solve():
    N = int(input())

    P = [1, 1]
    for i in range(2, N):
        P.append(P[i-1] + P[i-2])

    SP = [0]*(N)
    for i in range(N):
        SP[i] = SP[i-1] + P[i]

    dp = [0]*(N)
    dp[0] = 1
    if N == 1:
        return 1
    dp[1] = 2
    if N == 2:
        return 2
    dp[2] = 4

    for i in range(3, N):
        for x in range(N):
            if SP[x] > i:
                idx = x-1
                break

        if i in SP:
            idx = SP.index(i)
            dp[i] = 2**(idx+1)
        else:
            dp[i] = 2**(idx+1) + dp[i-SP[idx]-1]

    return dp[-1]


print(bin(solve())[2:])
