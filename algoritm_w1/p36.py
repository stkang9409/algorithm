N = int(input())
pay_table = []
for _ in range(N):
    row = list(map(int, input().split()))
    pay_table.append(row)


def move(start=0, end=0, total_pay=0, been=[False]*N, N=N, min_val=float('inf')):

    total_pay += pay_table[start][end]

    if False not in been[1:]:
        if pay_table[end][0] != 0:
            total_pay += pay_table[end][0]
            min_val = min(total_pay, min_val)
    else:
        for i in range(1, N):
            if not been[i]:
                if pay_table[end][i] == 0:
                    continue
                been[i] = True
                min_val = move(end, i, total_pay, min_val=min_val)
                been[i] = False

    return min_val


print(move())
