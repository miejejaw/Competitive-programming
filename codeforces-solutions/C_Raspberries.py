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
    n,k = IL()
    nums = IL()
    
    res = float("inf")
    count = 0
    for num in nums:
        rm = num%k
        if not rm:
            res = 0
        else:
            res = min(res, k - rm)
        
        if k == 4 and num%2 == 0:
            count += 1
            
    if k == 4:
        if count:
            res = min(res,0 if count > 1 else 1)
        else:
            res = min(res,2)
    
    print(res)

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())