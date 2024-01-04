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
    x,k = IL()

    for num in range(x,x+20):
        total = 0
        temp = num
        while num:
            total += num%10
            num //= 10
        
        if total%k == 0:
            return temp
    
# T = 1
T = I()
for _ in range(T):
    # solve()
    print(solve())