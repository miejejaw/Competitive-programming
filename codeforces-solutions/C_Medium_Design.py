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
    
    max_idx = 0
    min_idx = float("inf")
    prefix = defaultdict(int)
    for _ in range(n):
        a,b = IL()
        prefix[a] += 1
        prefix[b+1] -= 1
        max_idx = max(max_idx,b)
        min_idx = min(min_idx,a)
    
    _max = prev = 0
    _min = 0 if min_idx>1 or max_idx<m else float("inf")
    prefix.pop(max_idx+1)

    for idx in sorted(prefix):
        prev += prefix[idx]
        _max = max(prev,_max)
        _min = min(prev,_min)
        print(prev,_max,_min)
    
    print(_max - _min)


# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())