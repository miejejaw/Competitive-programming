from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def ss(s,n):
    for ind in range(n):
        s[ind] = "0"
    return "".join(s)

def solve():
    n = I()
    max_ = ["1" for _ in range(n//2)]
    if n%2 == 1:
        max_[0] = "7"
    max_ = "".join(max_)
    
     
    min_ = ["8" for _ in range(n//7)]
    
    rm = n%7 
    len_ = len(min_) 
    
    if rm == 6:
        min_ = "6"+"".join(min_)
    elif rm+len_ >= 5:
        min_ = "2"+ss(min_,5-rm)
    elif rm+len_ >= 4:
        min_ = "4"+ss(min_,4-rm)
    elif rm == 3:
        min_ = "7"+"".join(min_)
    elif rm +len_ >= 2:
        min_ = "1"+ss(min_,2-rm)
    else:
        min_ = "".join(min_)
    
    print(min_,max_)
    
# T = 1
T = I()
for _ in range(T):
    solve()