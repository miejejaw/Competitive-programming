class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m,n = len(dungeon),len(dungeon[0])
        grid = [[float("inf")]*(n+1) for _ in range(m+1)]

        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                _min = min(grid[row][col+1],grid[row+1][col])
                grid[row][col] = 0

                if _min == float("inf") and dungeon[row][col]<0:
                    grid[row][col] = abs(dungeon[row][col])
                elif dungeon[row][col] < _min and _min != float("inf"):
                    grid[row][col] = _min-dungeon[row][col]
                    
        return grid[0][0] + 1
