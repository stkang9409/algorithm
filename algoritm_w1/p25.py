w, h = map(int, input().split())
N = int(input())

# 0이면 가로 1이면 세로

# 자르면 배열로 들어감

cut_w = [0, w]
cut_h = [0, h]
for _ in range(N):
    t, n = map(int, input().split())
    if t == 0:
        cut_h.append(n)
    else:
        cut_w.append(n)

cut_h.sort()
cut_w.sort()

w = 0
h = 0

for i in range(1, len(cut_w)):
    w = max(w, (cut_w[i] - cut_w[i-1]))


for i in range(1, len(cut_h)):
    h = max(h, (cut_h[i] - cut_h[i-1]))

print(w*h)
