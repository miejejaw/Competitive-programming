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
    
    cards = ST()
    count = 0
    
    for ind in range(3):
        if ord(cards[ind]) != (97+ind):
            count += 1
    
    if count == 3:
        print("NO")
    else:
        print("YES")
        
# T = 1
T = I()
for _ in range(T):
    solve()