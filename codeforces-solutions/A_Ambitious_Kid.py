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
    ans = float("inf")
    for num in nums:
        ans = min(ans,abs(num))
    
    return ans

T = 1
# T = I()
for _ in range(T):
    # solve()
    print(solve())