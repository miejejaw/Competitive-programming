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
    res = [0]*2
    for ind in range(n):
        if nums[ind] > 0:
            res[ind%2] += nums[ind]
    
    ans = max(res)
    if ans == 0: ans = max(nums)
    print(ans)

# T = 1
T = I()
for _ in range(T):
    solve()