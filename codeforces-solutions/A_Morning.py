from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())
def STLN(): return list(map(int, input()))

def solve():
    nums = STLN()
    n = len(nums)
    for idx in range(n):
        if nums[idx] == 0:
            nums[idx] = 10
    
    count = 0
    prev = 0
    for num in nums:
        count += abs(num-prev) + 1
        prev = num
    
    print(count-1)



# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())