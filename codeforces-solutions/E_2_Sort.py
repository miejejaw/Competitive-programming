t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    
    beg,count = 0,0
    for end in range(1,n):
        if arr[end-1]>=arr[end]*2:
            beg = end
        if end-beg == k:
            count += 1
            beg += 1
        
    print(count)