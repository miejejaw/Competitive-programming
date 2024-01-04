t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    temp = arr[-2]
    count = 0
    for ind in range(len(arr)-2):
        if count+1==temp:
            break
        count += 1
    print(count)