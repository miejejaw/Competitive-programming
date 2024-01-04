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
    n,m,x = IL()
    ans = "NO"
    res = []
    
    if x != 1: 
        ans = "YES"
        res = [1]*n
    elif n%2 == 0 and m > 1:
        res = [2]*(n//2)
        ans = "YES"
    elif n%2 == 1 and m > 2:
        res = [2]*((n//2)-1)
        res.append(3)
        ans = "YES" 
        
        
    print(ans)
    if ans == "YES":
        print(len(res))
        print(*res)
        
# T = 1
T = I()
for _ in range(T):
    solve()