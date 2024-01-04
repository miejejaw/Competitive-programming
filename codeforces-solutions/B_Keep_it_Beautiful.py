from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    nums = IL()
    
    res = ["0"]*n
    res[0],ind = "1",1
    
    while ind<n and nums[ind-1]<=nums[ind]:
        res[ind] = "1"
        ind += 1
        
    while ind<n and nums[ind]>nums[0]:
        ind += 1
           
    prev = 0 
    for i in range(ind,n):
        if prev<=nums[i]<=nums[0]:
            res[i] = "1"
            prev = nums[i]
            
    print("".join(res))