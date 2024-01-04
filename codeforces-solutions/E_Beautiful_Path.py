import sys
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())
path = []
prev = []
ans = "NO"
i=j=-1
for _ in range(n):
    row = input()
    path.append(row)
    prev.append([-4]*m)
    if j==-1 and "S" in row:
        j = row.index("S")
        i = _
path = list(map(list,path))

def trav(row,col,way,turn,i,j):
    global ans,n,m,path,prev
    if not(0<=row<n) or not(0<=col<m) or ans=="YES" or path[row][col]=="*" or turn>2: 
        return
    if i>0 and prev[row][col]!=-4 and prev[row][col]<prev[i][j]:
        return
    if path[row][col]=='T':
        ans = "YES"
        return
    prev[row][col] = turn
    trav(row+1,col,"D",turn+(way!="D"),row,col)
    trav(row,col-1,"L",turn+(way!="L"),row,col)
    trav(row-1,col,"U",turn+(way!="U"),row,col)
    trav(row,col+1,"R",turn+(way!="R"),row,col)
    
trav(i,j,"O",-1,-1,-1)
print(ans)
    
    