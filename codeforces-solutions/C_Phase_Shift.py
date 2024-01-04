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
    n = I()
    t = ST()
    d = {}
    pr = {}
    s = ""
    visited = set()
    for ind in range(n):
        if t[ind] in d:
            s += d[t[ind]]
        else:
            for ch in range(97,123):
                if ch not in visited and t[ind] != chr(ch):
                    d[t[ind]] = chr(ch)
                    s += chr(ch)
                    visited.add(ch)
                    break
    print(s)

# T = 1
T = I()
for _ in range(T):
    solve()