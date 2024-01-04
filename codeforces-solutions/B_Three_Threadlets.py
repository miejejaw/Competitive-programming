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
    a,b,c = ILS()
    
    if a==b==c or (b==a and c%a==0 and c//a <= 4) or (b==2*a and c%a==0 and c//a <= 3):
        print("YES")
    else:
        print("NO")

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())