t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    w = min(a,b)+min(c,d)
    if w==max(a,b) and w==max(c,d):
        print("Yes")
    else:
        print("No")