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
    ans = float("inf")
    visited = {"00": 0}
    
    for _ in range(n):
        m,sk = input().split()
        temp = "1" if sk[0] == "0" else "0"
        temp += "1" if sk[1] == "0" else "0"
        
        if temp in visited:
            ans = min(ans,visited[temp]+int(m))
        
        if sk in visited:
            visited[sk] = min(visited[sk],int(m))
        else:
            visited[sk] = int(m)
    
    if ans == float("inf"):
        ans = -1
    print(ans)


# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())