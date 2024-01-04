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
    total = 0
    a = n - math.floor(math.sqrt(n))
    for i in range(1,a):
        total += i*i

    _max = 0
    b = n
    
    while a < b:
        total += 2*(a*b)
        _max = max(_max,a*b)
        a += 1
        b -= 1
        
    if a == b: total += a*b
    print(total - _max)


# T = 1
T = I()
for _ in range(T):
    solve()