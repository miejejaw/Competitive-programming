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
    n,d = IL()
    if d <= n:
        print("YES")
        return
    
    for num in range(1,n//2 + 1):
        if num + math.ceil(d/(num+1)) <= n:
            print("YES")
            return
    
    print("NO")

# T = 1
T = I()
for _ in range(T):
    solve()