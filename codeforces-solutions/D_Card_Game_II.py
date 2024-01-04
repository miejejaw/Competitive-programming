from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
mat = ILS()
ibs = ILS()
m,i = n-1,0
r = 0

for ind in range(n-1,-1,-1):
    
    while m>=0 and ibs[ind] < mat[m]:
        m -= 1
        if r: 
            r -= 1
            continue
        r += 1
        i += 1
        
    m -= 1
    if m<0: break   

        
print(i)