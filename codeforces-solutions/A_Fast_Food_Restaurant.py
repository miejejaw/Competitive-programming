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
    nums = ILS()
    count = 0
    for ind in range(3):
        if nums[ind]: 
            count += 1
            nums[ind] -= 1
    if nums[2] and nums[1]:
        count += 1
        nums[1] -= 1
        nums[2] -= 1
        
    if nums[2] and nums[0]:
        count += 1
        nums[0] -= 1
        nums[2] -= 1
    
    if nums[1] and nums[0]:
        count += 1
        nums[0] -= 1
        nums[1] -= 1
        
    if nums[1] and nums[0] and nums[0]:
        count += 1
        nums[0] -= 1
        nums[1] -= 1  
        nums[2] -= 1 
    
    print(count)     

# T = 1
T = I()
for _ in range(T):
    solve()