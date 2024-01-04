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
    
    w1 = ST()
    w2 = ST()

    m,n = len(w1),len(w2)
    
    a = m-1
    b = n-1
    
    for i in range(min(m,n)):
        if w1[a] != w2[b]:
            break
        b -= 1
        a -= 1
    
    return a+b+2
   
T = 1
# T = I()
for _ in range(T):
    print(solve())