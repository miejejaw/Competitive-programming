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
    
    prefix =  0
    for num in nums:
        if prefix+1 < num:
            break
        prefix += num
    
    print(prefix+1)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())