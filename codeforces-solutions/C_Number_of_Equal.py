n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

res = 0
left = 0
temp = 0
for ind,num in enumerate(arr2):
    if ind!=0 and arr2[ind-1]!=num:
        temp = 0
    while left<n and arr1[left]<num:
        left += 1
    while left<n and arr1[left]==num:
        left += 1
        temp += 1
    res += temp
print(res)