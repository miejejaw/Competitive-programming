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
    if n == 1:
        print(1)
    elif n == 2:
        print(2,1)
    else:
        ans = [0]*n
        ans[0] = 2
        ans[-1] = 3
        ans[n//2] = 1
        num = 4
        for i in range(1,n-1):
            if i != n//2:
                ans[i] = num
                num += 1
        print(*ans)

# T = 1
T = I()
for _ in range(T):
    solve()