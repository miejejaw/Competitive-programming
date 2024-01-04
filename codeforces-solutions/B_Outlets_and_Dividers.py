t  = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort(reverse=True)
    if n < 3:
        print(0)
        continue
    elif m > 0 and nums[0]+1 >= n:
        print(1)
        continue
    elif m > 1 and nums[0]+nums[1]>=n:
        print(1,2)
        continue
        
    ans = - 1
    if m > 1:
        n -= nums[0]+nums[1]
        ans = 2
    for ind in range(2,m):
        n -= nums[ind] - 1
        ans += 1
        if n <= 0:
           break
    print(ans)
        
    