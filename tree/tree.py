import sys
from string import ascii_uppercase

input = sys.stdin.readline

class Node():
    def __init__(self,value):
        self.value = value
        self.l = None
        self.r = None

class Tree():
    def __init__(self):
        self.root = None


def ps(node):
    if node == None:
        return
    
    print(node.value, end="")
    ps(node.l)
    ps(node.r)
    return

def ms(node):
    if node == None:
        return
    
    ms(node.l)
    print(node.value, end="")
    ms(node.r)
    return

def aas(node):
    if node == None:
        return
    
    aas(node.l)
    aas(node.r)
    print(node.value, end="")
    return

def solve():
    N = int(input())
    alphas = list(ascii_uppercase)
    nodes = {}
    
    for i in range(N):
        nodes[alphas[i]] = Node(alphas[i])
    
    for i in range(N):
        p, cl, cr = map(str, input().rstrip().split())
        nodes[p].l = nodes[cl] if cl != "." else None
        nodes[p].r = nodes[cr] if cr != "." else None
    
    ps(nodes["A"])
    print("")
    ms(nodes["A"])
    print("")
    aas(nodes["A"])

solve()