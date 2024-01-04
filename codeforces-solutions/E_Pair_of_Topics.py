n = int(input())
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))

nums = [0]*n
for ind in range(n):
    nums[ind] = arr_a[ind]-arr_b[ind]
nums.sort()

beg,end = 0,n-1
count = 0
while beg<end:
    if nums[end]>-nums[beg]:
        count += end-beg
        end -= 1
    else:
        beg += 1
print(count)
