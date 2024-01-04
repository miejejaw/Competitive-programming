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
    n,k = IL()
    nums = IL()
    if sum(nums) <= k:
        print(0)
        return
    
    num = 0
    _max = 0
    for ind in range(n):
        if k-nums[ind] < 0:
            if num != 0: break
            if _max <= nums[ind]:
                num = nums[ind]
                continue 
            
            k += _max
            if ind+1 >= n or k-nums[ind]-nums[ind+1] < 0:
                break
            num = _max
            k -= nums[ind]
        else:
            _max = max(_max,nums[ind]) 
            k -= nums[ind]  
                
    if num == 0: print(0)
    else:
        print(nums.index(num)+1)   
    

# T = 1
T = I()
for _ in range(T):
    solve()