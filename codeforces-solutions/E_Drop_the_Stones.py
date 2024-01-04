t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(input()))
        
    for col in range(m):
        beg,end = n-1,n-2
        while end>=0 and n>=0:
            if arr[beg][col]=="." and arr[end][col]=="*" and beg>end:
                arr[beg][col] = "*"
                arr[end][col] = "."
                
            while end>=0 and arr[end][col]!="*":
                if arr[end][col]=="o":
                    beg = end-1
                end -= 1
            while beg>=0 and arr[beg][col]!=".":
                beg -= 1
            if beg<end:
                end = beg-1
    for row in range(n):
        print("".join(arr[row]))
                
            
                