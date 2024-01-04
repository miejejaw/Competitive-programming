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
    ind = count = 0
    while ind < n:
        while ind<n and nums[ind] < 0:
            while ind<n and nums[ind] <= 0:
                nums[ind] = abs(nums[ind])
                ind += 1
            count += 1            
        ind += 1

    print(sum(nums),count)

# T = 1
T = I()
for _ in range(T):
    solve()