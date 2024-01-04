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
    
    ind = n-2
    while ind>=0 and nums[ind] <= nums[ind+1]:
        ind -= 1
    
    if ind < 0:
        print(0)
    else:
        print(max(nums[:ind+1]))
    



# T = 1
T = I()
for _ in range(T):
    solve()