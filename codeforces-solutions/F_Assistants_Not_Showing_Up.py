n,m = map(int,input().split())
nums = [0]*(n+1)
for _ in range(m):
    i,j=map(int,input().split())
    nums[i] += 1
    nums[j+1] -= 1
ans = "NO"
for ind in range(1,n):
    nums[ind] += nums[ind-1]
    
for ind in range(n):
    if nums[ind] == 0:
        ans = "YES"
        break
print(ans)