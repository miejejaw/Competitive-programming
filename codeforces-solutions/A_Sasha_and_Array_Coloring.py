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
    ans = 0
    for ind in range(n//2):
        ans += nums[~ind]-nums[ind]

    print(ans)

# T = 1
T = I()
for _ in range(T):
    solve()