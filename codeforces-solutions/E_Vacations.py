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
    
    prev = 0
    count = 0
    
    for idx in range(n):
        
        if nums[idx] == 0 or (prev == nums[idx] and prev in (1,2)):
            count += 1
            prev = 3
        elif prev == 1 and nums[idx] in (2,3):
            prev = 2
        elif prev == 2 and nums[idx] in (1,3):
            prev = 1
        else:
            prev = nums[idx]
    
    print(count)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())