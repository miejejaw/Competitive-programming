n = int(input())
arr = list(map(int,input().split()))

count = 1
ans = 0
for end in range(1,n):
    if arr[end-1]>arr[end]:
        ans = max(ans,count)
        count = 0
    count += 1
ans = max(ans,count)   
print(ans)