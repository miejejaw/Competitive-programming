from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    word = ST()
    ans = 0
    count = 0
    a,b = 0,0
    f = True
    for ind,ch in enumerate(word):
        if ch == "1":
            count += 1
        else:
            ans = max(ans,count)
            if f:
                a = count
            f = False
            count = 0
            
    b = count       
    ans = max(ans,count)    
    if a>0 and b>0:
        if a < b:
            ans = max(ans,b*b)
        elif a == b:
            ans = max(ans,b*(b+1))
    else:
        a = ans-1
        b = 2
        
    while b <= a:
        ans = max(ans,a*b)
        a -= 1
        b += 1
    print(ans)
    