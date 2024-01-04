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
    
    l = 0
    r = n-1
    arr1 = []
    arr2 = []
    
    while l < r:
        arr1 += [nums[r],nums[l]]
        arr2 += [nums[l],nums[r]]
        l += 1
        r -= 1
        
    if l == r:
        arr1 += [nums[l]]
        arr2 += [nums[l]]
    
    ans = True
    total = arr1[0]+arr1[1]
    for i in range(1,n):
        if total != arr1[i]+arr1[i-1]:
            ans = False
    
    if ans: return "Yes"
    
    ans = True
    total = arr2[0]+arr2[1]
    for i in range(1,n):
        if total != arr2[i]+arr2[i-1]:
            ans = False
    
    if ans: return "Yes"

    return "No"
    
# T = 1
T = I()
for _ in range(T):
    # solve()
    print(solve())