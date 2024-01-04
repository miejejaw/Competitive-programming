t = int(input())
for _ in range(t):
    n = int(input())
    nums = input()
    beg = 0
    end = n-1
    while beg<end:
        if nums[beg]!=nums[end]:
            beg += 1
            end -= 1
        else:
            break
        
    print(end-beg+1)
        