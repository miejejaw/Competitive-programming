from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    w1 = ST()
    w2 = ST()
    l1 = l2 = 0
    
    for ind in range(n):
        if w1[ind] != w2[ind]:
            l1 += 1
        if w1[ind] != w2[~ind]:
            l2 += 1
    
    ans = min(l1,l2)*2
    if ans > 0:
        if l1 < l2:
            if l1%2 == 1: ans -= 1
        elif l1 > l2:
            if l2%2 == 0: ans -= 1
        else: 
            ans -= 1
            
    if l1!=0 and l2 == 0: print(2)
    else:  print(ans)
    
            