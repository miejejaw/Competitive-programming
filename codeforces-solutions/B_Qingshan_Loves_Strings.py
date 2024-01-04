from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def check(s,n):
    one = zero = False
    for i in range(1,n):
        if s[i] == s[i-1]:
            if s[i] == "1":
                one = True
            else:
                zero = True
    return one,zero

def solve():
    n,m = IL()
    s = ST()
    t = ST()
    
    one,zero = check(s,n)
    
    if not one and not zero:
        return "Yes"
    if one and zero:
        return "No"
    
    o,z = check(t,m)
    if o or z:
        return "No"
    
    if (one and t[0] == t[-1] == "0") or (zero and t[0] == t[-1] == "1"):
        return "Yes"
    
    return "No"

# T = 1
T = I()
for _ in range(T):
    # solve()
    print(solve())