from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def helper(res,ind,tp,n,prev):
    if ind < n:
        prev = [float("inf"),ind]
        if res[ind][0] >= tp[ind]+abs(ind-prev[1]):
            prev = [tp[ind]+abs(ind-prev[1]),ind]
        res[ind] = prev[:]
        helper(res,ind+1,tp,n,prev)
        if ind+1 < n and res[ind] > res[ind+1]:
            res[ind] = res[ind+1][:]
            
    

def solve():
    n,k = IL()
    co = IL()
    tp = IL()
    res = [-1]*n
    for c in co:
      res[c-1] = c-1
    
    helper(res,0,tp,n) 
    for ind in range(n):
        print(res[ind][0],end=' ')

# T = 1
T = I()
for _ in range(T):
    ST()
    solve()
    