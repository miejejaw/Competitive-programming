t = int(input())
for _ in range(t):
    n,a = map(int,input().split())
    nums = list(map(int,input().split()))
    m = 0
    for i in range(n):
        if nums[m]+m>nums[i]+i:
            m = i
    a -= nums[m]+m+1
    if a<0:
        print(0)
        continue
    
    ans = 1
    nums[m] = 10**9+10
    for i in range(n):
        nums[i] += min(i+1,n-i)
    print(nums)
    for num in sorted(nums):
        a -= num
        if a<0:
            break
        ans += 1
        
    print(ans)