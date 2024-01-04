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
    
    adj = defaultdict(list)
    indegree = [0]*(n+1)
    for _ in range(m):
        a,b = IL()
        adj[a].append(b)
        adj[b].append(a)
        indegree[a] += 1
        indegree[b] += 1
    
    visited = set()
    count = 0
    for node in range(1,n+1):
        if node not in visited and indegree[node] == 2:
            queue = deque([(node,1)])
            visited.add(node)
            while queue:
                curr,c = queue.popleft()
                if indegree[curr] != 2: break
                
                for node2 in adj[curr]:
                    if node2 not in visited:
                        queue.append((node2,c+1))
                        visited.add(node2)
                        break
                    elif node == node2 and c >= 3:
                        count += 1
    
    print(count)
                    
T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())