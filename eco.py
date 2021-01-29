import sys

input = sys.stdin.readline

class Trie():

    def __init__(self):
        self.childs = {}
        self.val = ""
        self.dic = set()

    def get(self, words):
        self.words = set(words)
    
    def insert(self, s):
        cur_node = self
        for c in s:
            if c in cur_node.childs:
                cur_node = cur_node.childs[c]
            else:
                cur_node.childs[c] = Trie()
                cur_node.childs[c].val = cur_node.val + c
                if len(cur_node.childs) > 1:
                    for child in cur_node.childs.values():
                        self.dic.add(tuple((child.val)))
                elif cur_node.val in self.words:
                    self.dic.add(tuple((cur_node.childs[c].val)))
                cur_node = cur_node.childs[c]

def solve(n):
    tree = Trie()
    arr = []
    init = {}
    ans = 0
    for _ in range(n):
        s = input().rstrip()
        arr.append(s)
        tree.dic.add(s[0])
    tree.get(arr)
    tree.childs = init
    for s in arr:
        tree.insert(s)
    
    for word in arr:
        count = 0
        word = list(word)
        while word:
            if tuple(word) in tree.dic:
                count += 1
            word.pop()
        ans += count
    print("%.2f" %(ans/n))

while True:
    n = input().rstrip()
    if n:
        solve(int(n))
    else:
        break
