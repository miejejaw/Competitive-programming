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
    m = I()
    seats = [I() for _ in range(n)]
    seats.sort()
    max_seat = seats[-1]+m
    min_seat = seats[-1]
    for ind in range(n-1):
        if m <= 0: break
        m -= seats[-1]-seats[ind]
    
    if m > 0:
        min_seat += math.ceil(m/n)
    
    print(min_seat,max_seat)
        
T = 1
# T = I()
for _ in range(T):
    solve()