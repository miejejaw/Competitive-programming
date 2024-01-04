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
    nums = list(map(int,STL()))
    prefix = defaultdict(int)
    prefix[1] = 1
    total = count = 0
    for idx in range(n):
        total += nums[idx]
        count += prefix[total-idx]
        prefix[total-idx] += 1
    
    print( count)

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())