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
    odds,evens = [],[]
    
    for num in nums:
        if num%2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    
    print(*odds,*evens)


# T = 1
T = I()
for _ in range(T):
    solve()