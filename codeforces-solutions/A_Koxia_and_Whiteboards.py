from itertools import accumulate
from collections import defaultdict
from heapq import heapify,heappop,heappush

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n,m = IL()
    a = IL()
    heapify(a)
    b = IL()
    
    for ind in range(m):
        heappop(a)
        heappush(a,b[ind])    
    print(sum(a))
    