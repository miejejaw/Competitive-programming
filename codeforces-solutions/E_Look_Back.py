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
    
    count = 0
    prev = nums[0]
    for num in nums:
        if prev <= num:
            prev = num
        else:
            a = math.ceil(math.log(prev,2)) - math.floor(math.log(num,2))
            if pow(2,a-1) * num >= prev:
                prev = pow(2,a-1) * num
                count += (a-1)
            else:
                prev = pow(2,a) * num
                count += (a)
    
    print(count)

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())