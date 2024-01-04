n = int(input())
nums = list(map(int,input().split()))
nums.sort()
neg = 0 
ans = 0
if n%2==1 and nums[-1]<0:
    ans = 2
for i in range(n):
    if nums[i]<0:
        ans += abs(nums[i])-1
        neg += 1       
    elif nums[i]>0:
        ans += nums[i]-1
        if neg%2==1:
            neg += 1
            ans += 2
    else:
        ans += 1
        if neg%2==1:
            neg += 1
print(ans)