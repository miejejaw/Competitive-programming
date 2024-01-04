t = int(input())
for _ in range(t):
    dic = {}
    words = input().split()
    
    for word in words:
        num = ''
        for ch in word:
            if ch.isdigit():
                num += ch
        dic[int(num)] = word.replace(num,'')
    
    result = []
    for num,word in sorted(dic.items()):
        result.append(word)
    print(*result)


