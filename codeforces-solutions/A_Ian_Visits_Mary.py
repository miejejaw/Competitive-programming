import sys
sys.setrecursionlimit(1500)
from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    a,b = IL()
    
    if b != 1:
        print(2)
        if b == 2:
            print(1,b+2)
        else:
            print(1,b+1)
    else:
        print(1)
    print(a,b)
    
nums = [[1]*n for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0),(1, 1),(-1, 1),(1, -1),(-1, -1)]

def inbound(row, col):
    return (0 <= row < n) and (0 <= col < n)

for row,col in directions:
    x = ax
    y = by
    while inbound(x,y):
        nums[x][y] = 0
        x += row
        y += col

ans = False
def dfsKing(x,y,tx,ty):
    global ans
    
    if x == tx and y == ty:
        ans = True
        return
        
    nums[x][y] == 0
    for row,col in directions:
        row += x
        col += y
        
        if not ans and inbound(row,col) and nums[row][col]:
            nums[row][col] == 0
            dfsKing(row,col,tx,ty)
        
dfsKing(n-bx,by-1,n-cx,cy-1)  

if               
if ans:
    
    
    ans = 1  
seen = set() 
def dfs(emp,depth):
    global ans
    ans = max(ans,depth)
    for i in nums[emp]:
        if i not in seen:
            seen.add(i)
            dfs(i,depth+1)

for emp in nums:
    if emp not in seen:
        dfs(emp,1)
print(ans)
