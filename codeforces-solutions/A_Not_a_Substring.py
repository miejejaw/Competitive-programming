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
    s = ST()
    n = len(s)
    
    if s == "()":
        print("NO")
    elif ")(" not in s:
        print("YES")
        print("()"*n)
    else:
        print("YES")
        print("("*n + ")"*n)
        
# T = 1
T = I()
for _ in range(T):
    solve()