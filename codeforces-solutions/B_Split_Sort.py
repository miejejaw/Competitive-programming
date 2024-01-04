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
    nums = IL()
    
    seen = set({0})
    count = 0
    for num in nums:
        if num-1 not in seen:
            count += 1
        seen.add(num)
    
    print(count)  
    
# T = 1
T = I()
for _ in range(T):
    solve()