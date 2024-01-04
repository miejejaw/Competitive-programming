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
    cost = [0]*(n+1)
    a = [0]*(n+1)
    d = {}
    
    for ind,num in enumerate(nums):
        temp = (ind-d[num]-1)//2 if num in d else ind//2
        a[num] = min()
        cost[num] = max(cost[num],temp)
        d[num] = ind
        
    ans = n   
    for ind in range(1,k+1):
        if ind in d:
            cost[ind] = max(cost[ind],(n-d[ind]-1)//2)
            ans = min(ans,cost[ind])
            
    print(*cost)
    print(ans)


# T = 1
T = I()
for _ in range(T):
    solve()