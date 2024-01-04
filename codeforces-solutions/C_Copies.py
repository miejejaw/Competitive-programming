from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def solve():
    n,x,y = IL()
    if x == y:
        print(1 + math.ceil((n-1) / 2))
        return 
    
    if x > y: 
        x,y = y,x
        
    total = n*x
    left,right = 1,total//y
    
    while left <= right:
        mid = left + (right-left)//2
        if max(mid*y,(n-mid)*x) <= total:
            left = mid+1
            total = max(mid*y,(n-mid)*x)
        else:
            right = mid-1
    
    print(total)

    
T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())