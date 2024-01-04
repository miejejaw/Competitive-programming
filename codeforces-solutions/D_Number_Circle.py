n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = "YES"
arr[-1],arr[-2] = arr[-2],arr[-1]
if arr[-2]>=arr[-1]+arr[-3]:
    ans = "NO"

print(ans)
if ans=="YES":
    print(*arr)