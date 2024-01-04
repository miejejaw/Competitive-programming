from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

a,b = IL()
res = [b]
ans = True
while a < b:
    if b%2 == 0:
        b //= 2
        res.append(b)
    elif b%10 == 1:
        b //= 10
        res.append(b)
    else:
        ans = False
        break
    
if ans and a == b:
    print("YES")
    print(len(res))
    print(*reversed(res))
else:
    print("NO")

