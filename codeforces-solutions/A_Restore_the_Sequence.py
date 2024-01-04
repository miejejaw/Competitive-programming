t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    beg,end = 0,n-1
    res = []
    while beg<=end:
        if end>beg:
            res.append(nums[beg])
            res.append(nums[end])
            beg +=1
        else:
            res.append(nums[end])
        end -= 1
    print(*res)
        