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
    left,right = 1,n-1
    
    while left<n and nums[left]<=nums[left-1]:
        left += 1
    
    while right>0 and nums[right]>=nums[right-1]:
        right -= 1
        
    if left>right: print("YES")
    else: print("NO")
        
# T = 1
T = I()
for _ in range(T):
    solve()