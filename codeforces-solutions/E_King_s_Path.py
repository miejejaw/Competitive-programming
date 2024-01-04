from heapq import heapify,heappop,heappush
from queue import deque

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        ox,oy = self.findStarting(grid,rows,cols)
        queue = deque([(ox,oy,0)])
        
        while queue:
            x,y,p = queue.popleft()
                      
                      
                      
                    
    
    
    
        
    def findStarting(self, grid, rows, cols):
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "@":
                    return row,col