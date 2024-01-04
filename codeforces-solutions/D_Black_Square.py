n,m = map(int,input().split())
res = []
lx,rx,uy,by = m,0,n,0
for i in range(n):
    row = input()
    if row.find("B")!=-1:
        lx = min(lx,row.find("B"))
    rx = max(rx,row.rfind("B"))
    count = row.count("B")
    if count or res:
        res.append(count)
    if count:
        uy = min(i,uy)
        by = i
        
w = rx-lx+1
h = by-uy+1
l = max(w,h)
if not res:
    print(1)
elif l>n or l>m:
    print(-1)
else:
    ans = l*l - sum(res)
    print(ans)
