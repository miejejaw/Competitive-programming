from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import itertools
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def solve():
  n,m = IL()
  s = ST()
  nums = [0]+list(itertools.accumulate(list(map(int,s))))

  count = 0
  f = False
  
  for _ in range(m):
      l,r = IL()
      total = nums[r]-nums[l-1]
      if total <= r-l:
          if nums[r]-nums[r-total] < total:
              count += 1
              print(l,r)
              continue
          
      f = True
              
  if f: count += 1         
  print(count)
              

# T = 1
T = I()
for _ in range(T):
    solve()
    
    #0011001