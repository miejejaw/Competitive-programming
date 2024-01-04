from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

def solve(nums,rows,cols,row,col,x,y):
    total = 0
    while 0<=row<rows and 0<=col<cols:
        total += nums[row][col]
        row += x
        col += y
    return total
    

t = I()
for _ in range(t):
    n,m = IL()
    ans = 0
    nums = []
    for _ in range(n):
        nums.append(IL())
        if n == 1 or m == 1:
            ans = max(ans,max(nums[_]))
            
    if n>1 and m>1:
        forward,backward = {},{}
        for col in range(m):
            backward[(0,col)] = solve(nums,n,m,0,col,1,1)
            forward[(n-1,col)] = solve(nums,n,m,n-1,col,-1,1)
            
        for row in range(n):
            backward[(row,0)] = solve(nums,n,m,row,0,1,1)
            forward[(row,0)] = solve(nums,n,m,row,0,-1,1)
            
        for row in range(n):
            for col in range(m):
                a = min(row,col)
                b = min(col,n-1-row)
                total = backward[(row-a,col-a)] + forward[(row+b,col-b)] - nums[row][col]
                ans = max(ans,total)
            
    print(ans)
            
            
    