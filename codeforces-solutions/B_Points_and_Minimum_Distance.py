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
    
    arr = []
    left = 0
    right = 2*n-1
    
    prev_x = nums[0]
    prev_y = nums[-1]
    ans = 0
    
    while left < right:
        arr.append((nums[left],nums[right]))
        ans += abs(nums[left]-prev_x) + abs(nums[right]-prev_y)
        prev_x = nums[left]
        prev_y = nums[right]
        left += 1
        right -= 1
    
    print(ans)
    for co in arr:
        print(*co)
        

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())
    
