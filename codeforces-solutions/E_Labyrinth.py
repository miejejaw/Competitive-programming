from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def inbound(row, col,n,m):
    return 0 <= row < n and 0 <= col < m

def solve():
    n,m = IL()
    sr,sc= IL()
    left,right = IL()
    
    grid = [ST() for _ in range(n)]
    heap = [(-left,-right,sr-1,sc-1)]
    visited = set()
    dist = []
    for _ in range(n):
        temp = []
        for _ in range(m):
            temp.append([1,1])
        dist.append(temp)

    dist[sr-1][sc-1] = [left,right]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while heap:
        l,r,a,b = heappop(heap)
        if (a,b) in visited: continue
        visited.add((a,b))
        
        for x, y in directions:
            row, col = x+a, y+b
            if inbound(row,col,n,m) and grid[row][col] == "." and (row,col) not in visited:
                if (0,-1) == (x,y):
                    if l<0 and l < dist[row][col][0]:
                        dist[row][col][0] = l+1
                        heappush(heap, (l+1,min(r,dist[row][col][1]), row, col))
                elif (0,1) == (x,y):
                    if r<0 and r < dist[row][col][1]:
                        dist[row][col][1] =  r+1
                        heappush(heap, (min(l,dist[row][col][0]),r+1, row, col))
                else:
                    dist[row][col] = [l,r]
                    heappush(heap, (l,r,row,col))
    
    count = 0
    for row in range(n):
        for col in range(m):
            if dist[row][col] != [1,1]:
                count += 1

    print(count)

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())

 