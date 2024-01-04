from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
nums = IL()
rest = nums.count(0)
for ind in range(1,n-1):
    if nums[ind] == 3:
        if nums[ind-1] == 1 and nums[ind+1] == 2:
            rest += 1
        elif nums[ind-1] == 2 and nums[ind+1] == 1:
            rest += 1
            
for ind in range(1,n):
    if (nums[ind]==1 or nums[ind]==2) and nums[ind] == nums[ind-1]:
        rest += 1
            
print(rest)