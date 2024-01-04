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
    nums = [0]*n
    nums[0] = 1
    
    for ind in range(1,n):
        nums[ind] = nums[ind-1] + 2
    
    print(*nums)
        
   
# T = 1
T = I()
for _ in range(T):
    solve()