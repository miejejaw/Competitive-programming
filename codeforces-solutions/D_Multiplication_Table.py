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
    n,m,k = I()

    res = [1]*max(n,m)
    
    num = n*m
    p = 2
    while p*p <= num:
        while num%p == 0:
    


T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())