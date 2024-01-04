from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,m,p = IL()
grid = []
row,col = 0,0
for x in range(n):
    rows = ST()
    grid.append(list(rows))
    if "M" in rows:
        row,col = x,rows.index("M")

steps = IL()
directions = [(-1,0),(1,0),(0,-1),(0,1)]
def inbound(row,col):
    return 0<=row<n and 0<=col<m

for ind in steps:
    if ind:
        x = row + directions[ind-1][0]
        y = col + directions[ind-1][1]
        if inbound(x,y) and grid[x][y] == ".":
            row,col = x,y

seen = set()     
def dfs(row,col,count):
    seen.add((row,col))
    grid[row][col] = count
    for x,y in directions:
        x,y = x+row,y+col
        if inbound(x,y):
            if (grid[x][y] == "." or grid[x][y] == "M" or (grid[x][y] != "#" and count>int(grid[x][y]))) and count>0:
                dfs(x,y,count-1)
            
dfs(row,col,p)
print(len(seen))

    
