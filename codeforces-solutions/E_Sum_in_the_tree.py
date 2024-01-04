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
    parent = IL()
    sv = IL()
    
    adj = defaultdict(list)
    for child,par in enumerate(parent,1):
        adj[par-1].append(child)
    
    queue = deque([(0, sv[0])])
    ans = sv[0]
    
    while queue:
        curr, s = queue.popleft()
        
        for node in adj[curr]:
            temp = s
            if s > sv[node] and sv[node] != -1:
                return -1
            
            if sv[node] != -1:
                ans += (sv[node] - s)
                temp = sv[node]
            
            queue.append((node, temp))

    return ans

T = 1
# T = I()
for _ in range(T):
    # solve()
    print(solve())