import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    trie = {"len":0, "val":None ,"childs": {}}
    for _ in range(N):
        n, *data = map(str, input().split())
        n = int(n)

        tmp = trie
        for i in range(n):
            if data[i] not in tmp["childs"]:
                tmp["childs"][data[i]] = {
                "len": i,
                "val": data[i],
                "childs": {}
                }

            tmp = tmp["childs"][data[i]]
    
    stack = [trie]

    while stack:
        tmp = stack.pop()
        if tmp["val"]:
            print("--"*tmp["len"], end="")
            print(tmp["val"])
        for childs in sorted(tmp["childs"].items(), reverse=True):
            stack.append(childs[1])


solve()