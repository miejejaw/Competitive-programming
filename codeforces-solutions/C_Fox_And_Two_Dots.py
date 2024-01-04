from heapq import heapify,heappop,heappush
from queue import deque

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,m = IL()
nums = []
for _ in range(n):
    nums.append(ST())

dir = [(1,0),(0,1),(-1,0),(0,-1)] 
def inbound(row,col):
    return 0<=row<n and 0<=col<m

seen = set()
def dfs(row,col,syb,pr,pc):
    
    seen.add((row,col))
    for x,y in dir:
        x,y = row+x,col+y
        if inbound(x,y) and nums[x][y] == syb:
            if (x,y) in seen and pr != -1 and (x,y) != (pr,pc):
                print("Yes")
                exit()
            elif (x,y) not in seen:
                dfs(x,y,syb,row,col)
                        
for row in range(n):
    for col in range(m):
        syb = nums[row][col]
        if (row,col) not in seen:
            dfs(row,col,syb,-1,-1)            
                
print("No")
           