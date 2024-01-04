from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    word = list(input())
    dic = defaultdict(int)
    a = set()
    ans = 0
    for w in word:
        dic[w] += 1
        
    for w in word:
        a.add(w)
        dic[w] -= 1
        if dic[w] == 0:
            del dic[w]
   
        ans = max(ans,len(a)+len(dic))
            
    print(ans)
        
    