t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(input())
    b = list(input())
    a.sort()
    b.sort()
    res = []
    i,j=0,0
    flag = a[0]<b[0]
    while i<n and j<m:
        if flag:
            res.append(a[i])
            i += 1
            for ind in range(k-1):
                if i>=n or a[i]>b[j]:
                    break
                res.append(a[i])
                i += 1
        else:
            res.append(b[j])
            j += 1
            for ind in range(k-1):
                if j>=m or a[i]<b[j]:
                    break
                res.append(b[j])
                j += 1 
        flag = not flag

    print("".join(res))       
        