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
    n,m = IL()
    ts = IL()
    te = IL()
    
    # count = 0
    while n and m:
        x = ts.index(max(ts))
        y = te.index(max(te))
        temp = ts[x]
        ts[x] -= te[y]
        te[y] -= temp
        
        if ts[x] <= 0: n -= 1
        if te[y] <= 0: m -= 1
        # count += 1
        
    
    if m: print("Tenzing")
    elif n: print("Tsondu")
    else: print("Draw")
        
# T = 1
T = I()
for _ in range(T):
    solve()