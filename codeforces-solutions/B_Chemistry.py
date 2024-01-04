from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict,Counter
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def solve():
    n,k = IL()
    
    de = Counter(ST())
    count = 0
    for key,val in de.items():
        if val%2 == 1:
            count += 1
    
    if count <= k+1:
        print("YES")
    else:
        print("NO")


# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())