t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    
    if a<b and a<c and b<d and c<d:
        print("YES")
    elif c<a and c<d and a<b and d<b:
        print("YES")
    elif d<c and d<b and c<a and b<a:
        print("YES")
    elif b<d and b<a and d<c and a<c:
        print("YES")
    else:
        print("NO")