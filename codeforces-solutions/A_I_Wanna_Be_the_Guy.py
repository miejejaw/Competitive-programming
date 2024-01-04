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
    _,*x = IL()
    _,*y = IL()
    if len(set(x).union(set(y))) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")


T = 1
# T = I()
for _ in range(T):
    solve()