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
    n,a,q = IL()
    s = ST()
    
    if a == n: return "YES"
    if s.count("+")+a < n: 
        return "NO"
    
    for ch in s:
        if ch == "+":
            a += 1
        else:
            a -= 1
            
        if a == n: return "YES"
    
    return "MAYBE"
    
# T = 1
T = I()
for _ in range(T):
    print(solve())