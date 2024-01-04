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
    
    if n == 1 or n == 3:
        print(-1)
    else:
        ans = [i for i in range(n,0,-1)]
        if n%2 == 1:
            mid = n//2
            ans = ans[:mid] + ans[mid:][::-1]
        
        print(*ans)       



# T = 1
T = I()
for _ in range(T):
    solve()