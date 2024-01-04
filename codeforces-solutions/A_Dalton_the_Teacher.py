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
    count = 0
    for ind in range(n):
        if ind+1 == nums[ind]:
            count += 1
    
    print(math.ceil(count/2))
        
# T = 1
T = I()
for _ in range(T):
    solve()