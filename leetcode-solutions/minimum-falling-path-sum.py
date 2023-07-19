class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        length = len(matrix)
        grid = [[10000]*(length+1) for _ in range(length+1)]

        for row in range(length-1,-1,-1):
            for col in range(length-1,-1,-1):
                temp = min(grid[row+1][col-1],grid[row+1][col],grid[row+1][col+1])
                if temp == 10000: temp = 0
                grid[row][col] = matrix[row][col] + temp

        return min(grid[0])