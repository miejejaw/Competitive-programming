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
  arr = [0]*n
  for ind in range(n):
      d =  math.ceil(nums[ind]/k)
      arr[ind] = (nums[ind] - d*k , ind+1)
      
  arr.sort(key=lambda x: (-x[0],x[1]))
  i = 0
  for k,index in arr:
      nums[i] = index
      i += 1
  print(*nums)
  
# T = 1
T = I()
for _ in range(T):
    solve()
