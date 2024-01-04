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
    n = I()
    d = defaultdict(int)
    
    for _ in range(n):
        s,e = IL()
        d[s] += 1
        d[e] -= 1

    count = 0
    prefix = 0
    for k in sorted(d):
        prefix += d[k]
        count = max(count,prefix)

    print(count)
            
# T = 1
T = I()
for _ in range(T):
    solve()

