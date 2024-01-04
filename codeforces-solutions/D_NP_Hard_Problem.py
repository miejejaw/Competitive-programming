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
    n,k = IL()
    indegree = [0]*(n+1)
    adj = defaultdict(list)
    
    for _ in range(k):
        a,b = IL()
        indegree[a] += 1
        indegree[b] += 1
        
        adj[a].append(b)
        adj[b].append(a)
    
    arya = set()
    
    for idx in range(1,n+1):
        if indegree[idx] == 1:
            arya.add(idx)
            arya.update(adj[idx])
    
    if len(arya) < 2:
        print(-1)
        return
        
    arya = list(arya)
    pira = arya.pop(-1)
    
    print(1)
    print(pira)
    print(len(arya))
    print(*arya)
    
T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())