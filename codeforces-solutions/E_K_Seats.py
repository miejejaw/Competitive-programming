n,m,k = map(int,input().split())
arr = []
for _ in range(n):
    temp = list(input())
    arr.append(temp)
k -= 1
res = 0
for row in range(n):
    beg = 0
    for ind in range(m):
        if arr[row][ind]=="*":
            beg = ind+1
            
        if ind-beg ==k:
            res += 1
            beg += 1
            
for col in range(m):
    beg = 0
    for ind in range(n):
        if arr[ind][col]=="*":
            beg = ind+1
            
        if k and ind-beg ==k:
            res += 1
            beg += 1
print(res)