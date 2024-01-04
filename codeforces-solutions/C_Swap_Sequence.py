n = int(input())
nums = list(map(int,input().split()))
res = [(nums[i],i) for i in range(n)]    
res.sort()

ans = []
j = 0
for num,i in res:
    if j!=i and num!=nums[j] and i>j:
        ans.append((i,j))
        nums[i],nums[j] = nums[j],nums[i]
        print(nums)
    j += 1  
      
print(len(ans))
for a in ans:
    print(*a)