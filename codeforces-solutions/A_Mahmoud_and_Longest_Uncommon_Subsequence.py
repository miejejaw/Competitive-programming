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
    w1 = ST()
    w2 = ST()
    
    if w1 != w2:
        print(max(len(w1),len(w2)))
    else:
        print(-1)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())