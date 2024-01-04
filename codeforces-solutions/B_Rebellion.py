t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    count = 0
    beg,end = 0, n-1
    while beg<end:
        while beg<end and nums[beg] == 0:
            beg += 1
        while beg<end and nums[end] == 1:
            end -= 1
        if beg==end:
            break
        count += 1
        beg += 1
        end -= 1
    print(count)
        
        