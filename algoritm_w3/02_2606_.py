import sys
input = sys.stdin.readline

cpt_num = int(input())
N = int(input())
graph = [[] for _ in range(cpt_num+1)]

for _ in range(N):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


def find():
    stack = [1]
    visted = {}
    result = []
    while stack:
        cpt = stack.pop()
        if not visted.get(cpt):
            visted[cpt] = True
            result.append(cpt)
            stack.extend(graph[cpt])
    return len(result)-1


print(find())
