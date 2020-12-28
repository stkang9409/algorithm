def bin_search(a, key):
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr)//2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl < pr:
            break

    return -1
