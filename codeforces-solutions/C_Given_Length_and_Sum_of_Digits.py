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
    m,s = IL()

    if s==0 and m>1: 
        print(-1,-1)
        return 
    elif s==0:
        print(0,0)
        return 
        
    _min = _max = -1   
    nums = ["0"]*m

    for idx in range(m):
        if s <= 0: break
        
        if s >= 9:
            nums[idx] = "9"
            s -= 9
        else:
            nums[idx] = str(s)
            s = 0

        
    if s == 0:    
        _max = "".join(nums) 
        if nums[-1] == "0":
            for idx in range(m-2,-1,-1):
                if nums[idx] != "0":
                    nums[-1] = "1"
                    nums[idx] = str(int(nums[idx])-1)
                    break
        _min = "".join(nums[::-1])
    
    print(_min,_max)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())