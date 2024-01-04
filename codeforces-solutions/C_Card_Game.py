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

for ind in range(n-1,-1,-1):
    while m>=0 and ibs[ind] < mat[m]:
        m -= 1
    if m<0: break   
    i += 1

        
if i > n//2:
    print("YES")
else:
    print("NO")