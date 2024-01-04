t = int(input())
for _ in range(t):
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    seen = set(words)
    res = ["0"]*n
    for i,word in enumerate(words):
        size = len(word)
        for ind in range(size):
            if word[ind:] in seen and word[:ind] in seen:
                res[i] = "1"
                break
    print("".join(res))