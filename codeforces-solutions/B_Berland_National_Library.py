from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input().split())

def solve():
    n = I()
    capacity = 0
    total = 0
    visitor = set()
    
    for _ in range(n):
        op,id = STL()
        if op == "+":
            total += 1
            if capacity < total:
                capacity += 1
            visitor.add(id)
        else:
            if id in visitor:
                visitor.remove(id)
                total -= 1
            else:
                capacity += 1
    
    print(capacity)
            
T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())