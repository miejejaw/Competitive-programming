from itertools import accumulate
from collections import deque


def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

beg = ST()
end =  ST()
def inbound(r,c):
    return 0<=r<8 and 0<=c<8

bc,br = ord(beg[0])-97,8-int(beg[1])
tc,tr = ord(end[0])-97,8-int(end[1])

board = [[-1]*8 for _ in range(8)]
directions = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
board[br][bc] = 0
path = 1
queue = [(br,bc)]

while queue:
    temp = []
    f = False
    for r,c in queue:
        for x,y in directions:
            x,y = x+r,y+c
            if inbound(x,y) and board[x][y] == -1:
                board[x][y] = path
                if (x,y) == (tr,tc):
                    f = True
                    break
                temp.append((x,y))
        if f:
            break
    if f:
        break
    path += 1
    queue = temp
    
#L, R, U, D, LU, LD, RU or RD.
dir = {(1,0):"U",(0,1):"L",(-1,0):"D",(0,-1):"R",
       (-1,-1):"RD",(1,1):"LU",(1,-1):"RU",(-1,1):"LD"}
print(board[tr][tc])
num = board[tr][tc]
ans = []

while num:
    num -= 1
    for x,y in directions:
        x,y = x+tr,y+tc
        if inbound(x,y) and num == board[x][y]:
            ans.append(dir[(x-tr,y-tc)])
            tr,tc = x,y
            break
        
for path in reversed(ans):
    print(path)
            
    


    
    