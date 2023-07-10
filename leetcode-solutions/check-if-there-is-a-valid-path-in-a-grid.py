class UnionFind:
    def __init__(self, rows, cols):
        self.parent = []
        for row in range(rows):
            temp = []
            for col in range(cols):
                temp.append((row,col))
            self.parent.append(temp)

    def unionFind(self, row,col):
        if (row,col) != self.parent[row][col]:
            self.parent[row][col] = self.unionFind(*self.parent[row][col])
        return self.parent[row][col]

    def union(self, row1,col1, row2,col2):
        row1,col1 = self.unionFind(row1,col1)
        row2,col2 = self.unionFind(row2,col2)

        if row2 < row1 or (row1 == row2  and col2 < col1):
            row1,row2 = row2,row1
            col1,col2 = col2,col1
        
        self.parent[row2][col2] = (row1,col1)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        rows,cols = len(grid),len(grid[0])
        directions = [(1,0,"D"),(0,1,"R"),(-1,0,"U"),(0,-1,"L")]
        Union = UnionFind(rows,cols)
        for row in range(rows):
            for col in range(cols):
                for x,y,dire in directions:
                    x += row
                    y += col
                    if self.validate(grid,x,y,dire,rows,cols,grid[row][col]):
                        Union.union(row,col,x,y)

        return Union.unionFind(0,0) == Union.unionFind(rows-1,cols-1)

    def validate(self,grid,row,col,dire,rows,cols,street1):
        if not(0<=row<rows and 0<=col<cols): return False
        
        street2 = grid[row][col]
        if street1 == 1:
            if dire == "L" and (street2 == 1 or street2 == 4 or street2 == 6): return True
            if dire == "R" and (street2 == 1 or street2 == 3 or street2 == 5): return True
        elif street1 == 2:
            if dire == "U" and (street2 == 2 or street2 == 3 or street2 == 4): return True
            if dire == "D" and (street2 == 2 or street2 == 5 or street2 == 6): return True
        elif street1 == 3:
            if dire == "L" and (street2 == 1 or street2 == 4 or street2 == 6): return True
            if dire == "D" and (street2 == 2 or street2 == 5 or street2 == 6): return True
        elif street1 == 4:
            if dire == "R" and (street2 == 1 or street2 == 3 or street2 == 5): return True
            if dire == "D" and (street2 == 2 or street2 == 5 or street2 == 6): return True
        elif street1 == 5:
            if dire == "L" and (street2 == 1 or street2 == 4 or street2 == 6): return True
            if dire == "U" and (street2 == 2 or street2 == 3 or street2 == 4): return True
        elif street1 == 6:
            if dire == "R" and (street2 == 1 or street2 == 3 or street2 == 5): return True
            if dire == "U" and (street2 == 2 or street2 == 3 or street2 == 4): return True
            
        return False


















