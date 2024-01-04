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
    num = ST()
    one = num.index("1")
    seven = num.index("7") 
    
    if one < seven:
        print("17")
    else:
        print("71")
    
# T = 1
T = I()
for _ in range(T):
    solve()