from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))


def solve(nums,n):
    dic = defaultdict(int)
    ind = 0
    while ind < n:
        i = ind
        ind += 1
        while ind<n and nums[ind] == nums[i]:
            ind += 1
        
        dic[nums[i]] = max(dic[nums[i]],ind-i)
        
    return dic


t = I()
for _ in range(t):
    n = I()
    a = IL()
    b = IL()
    adic = solve(a,n)
    bdic = solve(b,n)
    
    ans = 0
    for k,v in adic.items():
        ans = max(ans,v+bdic[k])
    for k,v in bdic.items():
        ans = max(ans,v+adic[k])
        
    print(ans)