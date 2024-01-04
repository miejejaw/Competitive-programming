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
    s = ST()
    
    count = n-1
    for idx in range(n-2):
        if s[idx] == s[idx+2]:
            count -= 1
    
    print(count)

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())