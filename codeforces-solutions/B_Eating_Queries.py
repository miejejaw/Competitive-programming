from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
from itertools import accumulate
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def solve():
    n,q = IL()
    candies = list(accumulate(ILS()[::-1]))
    for ind in range(q):
        amount = I()
        left,right = 0,n-1
        while left < right:
            mid = left + (right-left)//2
            if candies[mid] >= amount: 
                right = mid
            else: 
                left = mid+1
                
        if candies[left]>=amount:
            print(left+1)
        else:
            print(-1)
        
# T = 1
T = I()
for _ in range(T):
    solve()