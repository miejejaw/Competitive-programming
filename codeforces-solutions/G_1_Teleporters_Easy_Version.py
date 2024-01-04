t = int(input())
for _ in range(t):
    n,a = map(int,input().split())
    nums = list(map(int,input().split()))
    
    for i in range(n):
        temp = min(i+1,n-i+1)
        nums[i] += temp
    nums.sort()  
    ans = 0
    for num in nums:
        a -= num
        if a<0:
            break
        ans += 1
        
    print(ans)