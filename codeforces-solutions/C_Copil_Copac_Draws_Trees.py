from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    seen = set()
    ans = 0
    for _ in range(n-1):
        a,b = IL()
        if a not in seen:
            ans += 1
            seen.add(a)
            seen.add(b)
    print(ans)
        