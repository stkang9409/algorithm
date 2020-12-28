def search(n, sx, sy, x=0, y=0, count=0, finish=[False]):
    if finish[0] == True:
        return
    if n == 0:
        if sx == x and sy == y:
            print(count)
            finish[0] = True
            return
        count += 1
    else:
        gap = 2**(n-1)
        one_pass = 2**(n*2 - 2)
        if sx < x+gap and sy < y+gap:
            count = search(n-1, sx, sy, x, y, count=count)
        elif sx < x+gap*2 and sy < y+gap:
            count = search(n-1, sx, sy, x+gap, y, count=count + one_pass*1)
        elif sx < x+gap and sy < y+gap*2:
            count = search(n-1, sx, sy, x, y+gap, count=count + one_pass*2)
        else:
            count = search(n-1, sx, sy, x+gap, y+gap,
                           count=count + one_pass*3)
    return count


n, x, y = map(int, input().split())
search(n, y, x)
