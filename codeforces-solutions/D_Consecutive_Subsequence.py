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
    
    index = count = 0
    d = defaultdict(int)
    for ind,num in enumerate(nums):
        d[num] = d[num-1]+1
        if d[num] > count:
            count = d[num]
            index = ind
    
    
    res = []
    num = nums[index]-count+1
    for ind in range(n):
        if num == nums[ind]:
            num += 1
            res.append(ind+1)
    
    print(count)
    print(*res)   

         
T = 1
# T = I()
for _ in range(T):
    solve()