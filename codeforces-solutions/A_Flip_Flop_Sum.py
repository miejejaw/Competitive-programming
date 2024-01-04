t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    total = sum(nums)
    ans = float("-inf")
    for ind in range(1,n):
        if nums[ind]<0 and nums[ind-1]<0:
            ans = max(ans,total+4)
            break
        elif nums[ind]>0 and nums[ind-1]>0:
            ans = max(ans,total-4)
        else:
            ans = max(ans,total)
            
    print(ans)