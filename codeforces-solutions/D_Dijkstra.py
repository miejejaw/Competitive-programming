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
    graph = defaultdict(list)
    for _ in range(m):
        a,b,w = IL()
        graph[a].append((b,w))
        graph[b].append((a,w))
    
    parent = [-1] * (n+1)
    distances = {node: float('inf') for node in graph}
    distances[1] = 0
    visited = set()
    heap = [(0, 1)]
    
    while heap:
        current_distance, current_node = heappop(heap)
        if current_node == n: 
            break
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(heap, (distance, neighbor))
                parent[neighbor] = current_node

    else:
        print(-1)
        return
       
    path = []
    node = n
    while node != -1:
        path.append(node)
        node = parent[node]

    print(*path[::-1])

T = 1
# T = I()
for _ in range(T):
    solve()