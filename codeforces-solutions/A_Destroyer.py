from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict,Counter
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def solve():
   n = I()
   nums = IL()
   
   cc = Counter(nums)
   ans = "YES"
   for num in range(1,max(nums)+1):
       if num-1 not in cc or cc[num-1] < cc[num]:
           ans = "NO"
           break
       
   print(ans)      

# T = 1
T = I()
for _ in range(T):
    solve()