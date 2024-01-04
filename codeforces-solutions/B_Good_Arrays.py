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
    nums = IL()
    one = nums.count(1)
    total = sum(nums)-(n-one)
    
    if n>1 and one*2 <= total:
        print("YES")
    else:
        print("NO")
    

# T = 1
T = I()
for _ in range(T):
    solve()