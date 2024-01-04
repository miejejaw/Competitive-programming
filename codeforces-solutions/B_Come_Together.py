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
    ax,ay = IL()
    bx,by = IL()
    cx,cy = IL()
    count = 0
    if bx<ax<cx or cx<ax<bx:
        if not(by<ay<cy or cy<ay<by):
            count += min(abs(ay-by),abs(ay-cy))
    elif by<ay<cy or cy<ay<by:
        if not(bx<ax<cx or cx<ax<bx):
            count += min(abs(ax-bx),abs(ax-cx))
    else:
        count += min(abs(ay-by),abs(ay-cy))
        count += min(abs(ax-bx),abs(ax-cx))
    
    print(count+1)

# T = 1
T = I()
for _ in range(T):
    solve()
    