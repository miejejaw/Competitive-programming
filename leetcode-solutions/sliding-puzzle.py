from copy import deepcopy
class Solution:
    def inbound(self, row, col):
        return 0<=row<2 and 0<=col<3

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        i = j = 0
        if 0 in board[0]:
            j = board[0].index(0)
        else:
            i = 1
            j = board[1].index(0)

        queue = deque([(board[:],0,(i,j))])
        visited = set({tuple(board[0]+board[1])})
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while queue:
            board,count,(i,j) = queue.popleft()
            if board == [[1,2,3],[4,5,0]]:
                print(board)
                return count
            count += 1

            for x,y in directions:
                x,y = i+x,j+y
                if self.inbound(x,y):
                    board[i][j],board[x][y] = board[x][y],board[i][j]
                    if tuple(board[0]+board[1]) not in visited:
                        queue.append((deepcopy(board),count,(x,y)))
                        visited.add(tuple(board[0]+board[1]))
                    board[i][j],board[x][y] = board[x][y],board[i][j]

        return -1

             

