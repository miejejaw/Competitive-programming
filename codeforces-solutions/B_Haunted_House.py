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
    nums = ST()
    one = nums.count("1")
    
    res = [-1]*n
    for idx in range(n):
        



# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())