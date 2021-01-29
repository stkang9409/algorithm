from collections import deque

def solution(n):
    ans = 0
    q = deque()

    q.append([3,4,5])

    while q:
        A = q.popleft()
        l = len(A)
        if A[-1] == n:
            ans += 1
        
        if A[-1] < n:
            for i in range(l):
                val = A[i]*2 + A[l-1] + 2

                new = A[:] + [0,0,0]
                # new[i+1] 부터 바뀌어야함

                new[i+1] = new[i]*3
                new[i+2] = new[i+1] + 1
                new[i+3] = new[i+2] + 1
                for j in range(i+4, l+3):
                    if A[j-3]%3:
                        new[j] = new[j-1] + 1
                    else:
                        new[j] = 3*new[j-1]
                q.append(new)

    print(ans)
    return ans

solution(int(input()))