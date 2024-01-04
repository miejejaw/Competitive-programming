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
    nums = ILS()
    
    for idx in range(n-1):
        if nums[idx+1]-nums[idx] > 1:
            return "NO"
    
    return "YES"

# T = 1
T = I()
for _ in range(T):
    # solve()
    print(solve())