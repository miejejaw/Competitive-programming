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
    a = ST()
    b = ST()
    
    n = len(b)
    ind = n
    for idx in range(n):
        if a[idx] != b[idx]:
            ind = idx
            break
        
    if a[ind+1:] == b[ind:] or n == ind:
        beg = end = ind
        while beg>0 and a[beg] == a[beg-1]:
            beg -= 1

        while end<n and a[end] == a[end+1]:
            end += 1
    
        print(end-beg+1)
        for idx in range(beg,end+1):
            print(idx+1,end=" ")
    else:
        print(0)
        
                



T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())