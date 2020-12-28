N = int(input())
MAX_LEN = 50
container = [[] for _ in range(MAX_LEN+1)]
dic = {}

for _ in range(N):
    word = input()
    word_len = len(word)
    is_registered = dic.get(word)
    if not is_registered:
        container[word_len].append(word)
        dic[word] = True

for words in container:
    words.sort()
    if len(words) != 0:
        for word in words:
            print(word)
