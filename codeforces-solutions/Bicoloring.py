from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def solve(n):
    edges = I()
    adj = defaultdict(list)
    for _ in range(edges):
        node1,node2 = IL()
        adj[node1-1].append(node2-1)
        adj[node2-1].append(node1-1)
        
    color = [0]*n
    queue = deque([0])
    visited = set({0})
    color[0] = 1
    ans = "BICOLOURABLE."
    
    while queue:
        curr = queue.popleft()
        for node in adj[curr]:
            if node in visited:
                if color[curr] == color[node]:
                    ans = "NOT BICOLOURABLE."
                    break
                else:
                    continue
            queue.append(node)
            visited.add(node)
            color[node] = 1 if color[curr] == 2 else 2
        if ans == "NOT BICOLOURABLE.": break       
    print(ans)
    n = I()
    if n: solve(n)


T = 1
# T = I()
for _ in range(T):
    n = I()
    solve(n)