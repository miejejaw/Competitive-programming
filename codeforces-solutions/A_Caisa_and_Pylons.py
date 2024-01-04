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
    
    total = nums[0]
    curr = 0
    
    for idx in range(n-1):
        if nums[idx] < nums[idx+1]: 
            curr -= (nums[idx+1]-nums[idx])
            if curr < 0:
                total += abs(curr)
                curr = 0    
        else:
            curr += (nums[idx]-nums[idx+1])
    
    print(total)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())