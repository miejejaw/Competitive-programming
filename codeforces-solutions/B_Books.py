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
    n,t = IL()
    nums = IL()
    beg = count = 0
    for end in range(n):
        t -= nums[end]
        while beg<=end and t<0:
            t += nums[beg]
            beg += 1
        
        count = max(count,end-beg+1)

    print(count)

T = 1
# T = I()
for _ in range(T):
    solve()