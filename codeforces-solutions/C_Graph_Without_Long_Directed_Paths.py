from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

adList = defaultdict(list)

n,m = IL()
for i in range(1,m+1):
    node1,node2 = IL()
    adList[node1].append((node2,i))
    adList[node2].append((node1,-i))

res = ["1"]*m
queue = deque([(1,1)]) 
visited = {1:1}  

while queue:
    curr,color = queue.popleft()
    for node,idx in adList[curr]:
        if node not in visited:
            queue.append((node,-color))
            visited[node] = -color
            
            ind = abs(idx)-1
            temp = color if idx > 0 else -color
            if temp < 0:
                res[ind] = "0"
        elif color == visited[node]:
            print("NO")
            exit()
               
print("YES")
print("".join(res))

        