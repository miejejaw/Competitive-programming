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
    nums = ILS()[::-1]
    
    num,freq = nums[0],1
    beg = 0

    for end in range(1,n):
        k -= (nums[beg]-nums[end])
        
        while beg<end and k < 0:
            k += (nums[beg]-nums[beg+1]) * (end-beg)
            beg += 1

        if end-beg+1 >= freq:
            num = nums[beg]
            freq = end-beg+1
                   
    print(freq,num)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())