n = int(input())
arr = list(map(int,input().split()))
arr.sort()
if arr[0]==arr[-1]:
    print(-1)
else:
    print(*arr)