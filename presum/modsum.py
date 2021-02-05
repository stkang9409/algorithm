import sys

input = sys.stdin.readline

def solve():
	N, M = map(int, input().split())
	arr = list(map(int, input().split()))
	mod = [0] * M

	dp = [0] * (N+1)
	for i in range(N):
		dp[i+1] = dp[i] + arr[i]

	for j in range(N+1):
		mod[dp[j]%M] += 1

	total = 0
	for m in mod:
		if m > 0:
			total += m*(m-1)/2
	print(int(total))

	return

solve()
