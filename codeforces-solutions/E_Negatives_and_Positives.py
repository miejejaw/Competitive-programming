t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    for ind in range(1,n):
        if nums[ind]<0 and nums[ind-1]<0:
            nums[ind] = -nums[ind]
            nums[ind-1] = -nums[ind-1]
        elif nums[ind]<0 and nums[]