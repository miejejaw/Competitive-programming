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
    nums = [(-num,idx+1) for idx,num in enumerate(nums) if num]
    heapify(nums)
    n = len(nums)
    
    res = []
    while n > 1:
        num1 = heappop(nums)
        num2 = heappop(nums)
         
        if num1[0]+1 < 0:
            heappush(nums,(num1[0]+1,num1[1]))
            n += 1
        
        if num2[0]+1 < 0:
            heappush(nums,(num2[0]+1,num2[1]))
            n += 1
            
        n -= 2
        res += [(num2[1],num1[1])]
        
    print(len(res))
    for a,b in res:
        print(a,b)

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())
    
