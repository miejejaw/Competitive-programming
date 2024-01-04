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
    
    fir = ST()
    res = fir[0]+fir[2]
    if fir[1] == ">":
        res = fir[2]+fir[0]
         
    sec = ST()
    temp = sec[0]+sec[2]
    if sec[1] == ">":
        temp = sec[2]+sec[0]
        
    if res[0] in temp:
        res = temp+res[1] 
    else:
        res = res[0]+temp
         
    rd = ST()
    temp = rd[0]+rd[2]
    if rd[1] == ">":
        temp = rd[2]+rd[0]
    x,y = res.index(temp[0]),res.index(temp[1])
    
    if x!=0 and y!=0: 
        res = res[0]+temp
        print(res)
    elif x!=2 and y!=2:
        res = temp + res[2]
        print(res)
    elif x>y:
        print("Impossible")
    else:
        print(res)

T = 1
# T = I()
for _ in range(T):
    solve()