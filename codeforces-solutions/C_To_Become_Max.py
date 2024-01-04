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
    ans = max(nums)
    for i in range(n-2,-1,-1):
        if nums[i] <= nums[i+1]:
            prev = nums[i+1]
            temp = k
            for j in range(i,-1,-1):
                if prev-nums[j]+1 > temp:
                    break
                temp -= (prev-nums[j]+1)
                prev += 1
            ans = max(ans,prev)

    print(ans)
           
# T = 1
T = I()
for _ in range(T):
    solve()