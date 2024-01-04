t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(sorted(map(int,input().split())))
    beg,end = 0,n-1
    blue,red = nums[0],nums[-1]
    res = "NO"
    while beg<end:
        if beg+1 <= n-end:
            beg += 1
            blue += nums[beg]
        elif blue >= red:
            end -= 1
            red += nums[end]
        else:
            res = "YES"
            break
    print(res)