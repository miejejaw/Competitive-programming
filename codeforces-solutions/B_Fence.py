from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,k = IL()
nums = IL()
total = sum(nums[:k])
ans = 0
temp = total

for ind in range(k,n):
    total = total - nums[ind-k]+nums[ind]
    if total < temp:
        temp = total
        ans = ind-k+1

print(ans+1)