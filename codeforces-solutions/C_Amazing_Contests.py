n = int(input())
arr = list(map(int,input().split()))
max_num = arr[0]
min_num = arr[0]
count = 0
for num in arr:
    if num>max_num:
        max_num = num
        count += 1
    elif min_num>num:
        min_num = num
        count += 1
print(count)