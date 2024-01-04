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
    
    n,k,x = IL()
    total = (n*(1+n)) // 2
    
    if total >= x:
        total =  (k*(n-k+1+n)) // 2
        if total >= x:
            return "YES"
    
    return "NO"
   
# T = 1
T = I()
for _ in range(T):
    print(solve())