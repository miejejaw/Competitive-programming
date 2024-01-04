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
    nums = ILS()
    
    c = [nums[-1]]
    ind = n-2
    while ind>=0 and nums[ind]==nums[-1]:
        c.append(nums[ind])
        ind -= 1
    if ind<0:
        print(-1)
        return
    
    b = nums[:ind+1]
    
    print(len(b),len(c))
    print(*b)
    print(*c)
    

# T = 1
T = I()
for _ in range(T):
    solve()