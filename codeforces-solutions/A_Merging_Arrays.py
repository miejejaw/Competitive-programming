n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

first,second = 0,0
res = []
while first<n and second<m:
    if arr1[first]<=arr2[second]:
        res.append(arr1[first])
        first += 1
    else:
        res.append(arr2[second])
        second += 1
res += arr1[first:]
res += arr2[second:]
print(*res)

1) Divide Players Into Teams of Equal Skill