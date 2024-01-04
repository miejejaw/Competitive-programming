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
    s = ST()
    
    ans = 0
    beg = 0
    temp = k
    for end in range(n):
        if s[end] == "b": temp -= 1
        while beg<end and temp<0:
            if s[beg] == "b":
                temp += 1
            beg += 1
        ans = max(ans,end-beg+1)
    
    beg = 0
    temp = k
    for end in range(n):
        if s[end] == "a": temp -= 1
        while beg<end and temp<0:
            if s[beg] == "a":
                temp += 1
            beg += 1
        ans = max(ans,end-beg+1)
    
    
    print(ans)



T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())