from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def ss(arr):
    a = b = float("inf")
    for num in arr:
        if a > num:
            b = a
            a = num
        elif b > num:
            b = num
     
    return (a,b)
    

def solve():
    n = I()
    total = 0
    xmin = float("inf")
    ymin = float("inf")
    for _ in range(n):
        m = I()
        arr = IL()
        a,b = ss(arr)
        xmin = min(xmin,a)
        ymin = min(ymin,b)
        total += b
    
    print(total+xmin-ymin)    

# T = 1
T = I()
for _ in range(T):
    solve()