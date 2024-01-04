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
    x,y,k = IL()
    
    ans = 0
    if y <= x:
        ans = x
    elif x+k >= y:
        ans = y
    else:
        ans = x+k + (y-(x+k)) * 2
        
    print(ans)


# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())