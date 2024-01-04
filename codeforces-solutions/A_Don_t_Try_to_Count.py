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
    n,m = IL()
    x = ST()
    s = ST()
    
    if s in x: return 0
    if n>=m and s in x+x: return 1
    
    count = 0
    while s not in x and n <= 2*m:
        x += x
        count += 1
        n += n
        
    if s in x:
        return count
        
    return -1
# T = 1
T = I()
for _ in range(T):
    # solve()
    print(solve())