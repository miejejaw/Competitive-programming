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
    x,y,n = IL()
    res = [0]*n
    res[-1] = y
    
    num = 1
    for ind in range(n-2,-1,-1):
        res[ind] = res[ind+1]-num
        num += 1
    
    if res[0] >= x:
        res[0] = x
        print(*res)
    else:
        print(-1)
         
# T = 1
T = I()
for _ in range(T):
    solve()