
import sys
sys.setrecursionlimit(5000)
from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def dfs(adj,color,curr):
    
    res = [0,0,0]
    for node in adj[curr]:
        temp = dfs(adj,color,node)
        res[0] += temp[0]
        res[1] += temp[1]
        res[2] += temp[2]
    
    if color[curr] == "B": res[0] += 1
    else: res[1] += 1
    if res[0] == res[1]: res[2] += 1
    return res

def solve():
    n = I()
    parents = IL()
    color = ST()
    adj = defaultdict(list)
    for node in range(n-1):
        adj[parents[node]-1].append(node+1)
    
    print(dfs(adj,color,0)[2])   
    
# T = 1
T = I()
for _ in range(T):
    solve()