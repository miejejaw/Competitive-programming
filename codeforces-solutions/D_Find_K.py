t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    seen = set()
    ans = "NO"
    for ind in range(n):
        if k+arr[ind] in seen or arr[ind]-k in seen:
            ans = "YES"
            break
        seen.add(arr[ind])
    print(ans)