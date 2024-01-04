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
   candy = IL()
   alice = bob = 0
   left,right = 0,n-1
   count = 0
   
   while left<=right:
        
       if alice <= bob:
           alice += candy[left]
           left += 1
       else:
           bob += candy[right]
           right -= 1
           
       if alice == bob:
           count = left + (n-right-1)
              
   print(count)

# T = 1
T = I()
for _ in range(T):
    solve()