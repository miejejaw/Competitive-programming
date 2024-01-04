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
    n,k = IL()
    nums = IL()
    
    if k in nums:
        return "YES"
    return "NO" 
   
# T = 1
T = I()
for _ in range(T):
    print(solve())