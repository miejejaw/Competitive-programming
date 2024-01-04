from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def make_grid_prefix(grid,rows,cols):
    
    for row in range(1,rows):
        for col in range(1,cols):
            grid[row][col] += (grid[row][col-1]+ grid[row-1][col] - grid[row-1][col-1])
            
def solve():
    chairs, hours  = IL()

    grid = [[0] * (102) for _ in range(102)]

    for _ in range(chairs):
        row, col = IL()
        grid[row+1][col+1] += 1

    make_grid_prefix(grid,102,102)
    
    for _ in range(hours):
        x1,y1,x2,y2 = IL()
        count = grid[x2+1][y2+1] + grid[x1][y1] - (grid[x2+1][y1] + grid[x1][y2+1])
        print(count)    

T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())
