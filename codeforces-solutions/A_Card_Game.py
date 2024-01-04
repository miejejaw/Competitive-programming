n = int(input())
arr = list(map(int,input().split()))
beg ,end = 0, n-1
wube = hen = 0
flag = True
while end>=beg:
    temp = 0
    if arr[end]>arr[beg]:
        temp = arr[end]
        end -=1
    else:
        temp = arr[beg]
        beg += 1
        
    if flag:
        wube += temp
    else:
        hen += temp
    flag = not flag
    
print(wube,hen)