from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

T = I()
for _ in range(T):
    n,m = IL()
    if m == 1:
        print(1,0)
        continue
    elif m == 2:
        print(1,1)
        continue
        
    d = defaultdict(int)
    for _ in range(m):
        a,b = IL()
        d[a] += 1 
        d[b] += 1
        
    count = defaultdict(int)
    for k,v in d.items():
        if v > 1:
            count[v] += 1
        
    if len(count) == 2:
        x,y = 0,0
        for k,val in count.items():
            if val == 1:
                x = k
            if val > 1:
                y = k-1
        print(x,y)
    else: 
        for k,v in count.items():
            print(k,k-1)
            
    
       
    
        