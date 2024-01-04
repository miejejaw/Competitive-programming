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
    res = [0]*(n)
    for ind in range(n):
        res[ind] = n - nums[ind] +1
        
        
    print(*res)
    