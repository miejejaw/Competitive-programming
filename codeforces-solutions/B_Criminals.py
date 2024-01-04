t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    beg = 0
    res = 0
    for end in range(1,n):
        while beg<n and nums[beg] == 0:
            beg += 1
        if beg == n:
            break
        if beg<end and nums[end] == 0:
            nums[end] = 1
            nums[beg] -= 1
            res += 1
    res += sum(nums[:n-1])
    print(res)
