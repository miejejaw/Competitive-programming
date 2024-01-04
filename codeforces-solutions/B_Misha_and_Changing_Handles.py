from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def dfs(d,username):
    if username in d:
        return dfs(d,d[username]) 
    return username

def solve():
    
    n = I()
    d = {}
    visited = set()
    
    for _ in range(n):
        old,new = input().split()
        d[old] = new
        visited.add(new)
    
    ans = {}
    for old in d:
        if old not in visited:
            ans[old] = dfs(d,old)
 
    print(len(ans))           
    for k,v in ans.items():
        print(k,v)   
        
T = 1
# T = I()
for _ in range(T):
    solve()