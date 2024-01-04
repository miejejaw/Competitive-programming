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
    n,m = IL()
    cats = [0]+IL()
    
    adj = defaultdict(list)
    for _ in range(n-1):
        a,b = IL()
        adj[a].append(b)
        adj[b].append(a)
    
    queue = deque([(1,cats[1])])
    visited = set({1})
    ans = 0
    
    while queue:
        curr,count = queue.popleft()
        isleaf = True
        for node in adj[curr]:
            if node not in visited:
                temp = count+1 if cats[node] else 0
                if temp <= m:
                    queue.append((node,temp))
                visited.add(node)
                isleaf = False
        
        if isleaf:
            ans += 1
    
    print(ans)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())