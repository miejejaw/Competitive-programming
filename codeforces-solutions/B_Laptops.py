n = int(input())
arr = []
for _ in range(n):
    p,q = map(int,input().split())
    arr.append((p,q))
arr.sort()

ans = "Poor Alex"
for i in range(1,n):
    if arr[i-1][1]>arr[i][1]:
        ans = "Happy Alex"
        break
print(ans)