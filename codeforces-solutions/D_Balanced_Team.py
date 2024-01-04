n = int(input())
arr = list(map(int,input().split()))
arr.sort()

beg,ans = 0,1
for end in range(1,n):
    while arr[end]>arr[beg]+5:
        beg += 1
    ans = max(ans,end-beg+1)
print(ans)