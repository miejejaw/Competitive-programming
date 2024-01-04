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
    res = [1]*k
    if n == k:
        print("YES")
        print(*res)
        return 
    
    count = 0
    num = n
    
    while num>1:
        count += 1
        num //= 2
    
    beg = 0
    if n%2 == 1:
        beg = 1 
        
    if beg<k:           
        res[beg] = pow(2,count)
    
    print(res[beg])
        
    for ind in range(beg+1,k):
        while beg<ind and res[beg]==1:
            beg += 1 
            
        if res[beg]>=2:
            res[beg] //= 2
            res[ind] = res[beg]
        else:
            break
            
    res.sort()
    print(*res)
    if sum(res) == n:
        print("YES")
    else:
        print("NO")
        
T = 1
# T = I()
for _ in range(T):
    solve()