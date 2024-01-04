t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    nums = list(map(int,input().split()))
    for _ in range(q):
        a,*b =  list(map(int,input().split()))
        if a==2:
            print(nums[b[0]-1])
        else:
            for i in range(b[0]-1,b[1]):
                total = 0
                while nums[i]:
                    total += nums[i]%10
                    nums[i] //= 10
                nums[i] = total
            
        