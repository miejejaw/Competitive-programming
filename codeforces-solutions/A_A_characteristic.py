from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n,k = IL()
    res = [1]*n
    n -= 1
    total = n*(1+n)//2
    ind = 0
    while n>0 and total != k:
        res[n] = -1
        total += ind - n
        ind += 1
        n -= 1      
    if total == k: 
        print("YES")
        print(*res)
    else:
        print("NO")

        