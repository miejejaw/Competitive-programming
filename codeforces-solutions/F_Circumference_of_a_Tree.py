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
    adj = defaultdict(list)
    indegree = [0]*(n+1)
    for _ in range(n-1):
        a,b = IL()
        adj[a].append(b)
        adj[b].append(a)
        indegree[a] += 1
        indegree[b] += 1
    
    queue = deque()
    visited = set()
    for node in range(n+1):
        if indegree[node] == 1:
            queue.append((node,0))
            visited.add(node)
            
    ans = 0
    distance = [0]*(n+1)
    while queue:
        curr,dis = queue.popleft()
        for node in adj[curr]:
            indegree[node] -= 1
            ans = max(ans,distance[node]+dis+1)
            distance[node] = max(distance[node],dis+1)
            
            if indegree[node] == 1 and node not in visited:
                queue.append((node,distance[node]))
                visited.add(node)  

    print(ans*3)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())