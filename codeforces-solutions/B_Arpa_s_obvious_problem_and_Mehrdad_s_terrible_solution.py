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
    n,x = IL()
    nums = IL()
    
    ans = 0
    d = defaultdict(int)
    for num in nums:
        if num^x in d:
            ans += d[num^x]
        
        d[num] += 1
    
    print(ans)
         
T = 1
# T = I()
for _ in range(T):
    solve()