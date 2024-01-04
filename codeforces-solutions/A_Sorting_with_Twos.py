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
    
    prev = 2
    for idx in range(3,n):
           
        if idx>prev and nums[idx-1] > nums[idx]:
            return "NO"
        
        if idx+1 == prev*2:
            prev *= 2     
    
    return "YES"

# T = 1
T = I()
for _ in range(T):
    # solve()
    print(solve())