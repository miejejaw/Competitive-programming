t = int(input())
for _ in range(t):
    word = input()
    res = set()
    ind,size = 0,len(word)
    while ind < size:
        if ind+1<size and word[ind]==word[ind+1]:
            ind += 2
        else:
            res.add(word[ind])
            ind += 1
                          
    res = sorted(res)
    print("".join(res))
