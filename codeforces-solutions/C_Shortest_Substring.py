n = int(input())
for _ in range(n):
    nums = input()
    nums = list(nums)
    nums = list(map(int,nums))
    arr = [-1]*4
    beg = 0
    end = 0
    ans = len(nums)+1
    while end <(len(nums)):
        arr[nums[end]] = end
        if arr[1]!=-1 and arr[2]!=-1 and arr[3]!=-1:
            ans = min(ans,end-beg+1)
            
            if arr[nums[beg]]==beg:
                arr[nums[beg]] = -1
            end -= 1
            beg += 1
            while beg+1<len(nums) and nums[beg] == nums[beg+1]:
                beg += 1
        end += 1
        
        
        
    if ans >len(nums):
        print(0)
    else:
        print(ans)
            