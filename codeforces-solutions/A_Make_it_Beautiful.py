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
    nums = IL()[::-1]
    if n > 2:
        nums[1],nums[-1] = nums[-1],nums[1]
       
    if n > 1 and nums[0] == nums[1]:
        print("NO")
    else:
        print("YES")
        print(*nums)

# T = 1
T = I()
for _ in range(T):
    solve()