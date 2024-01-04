a,b,c = map(int,input().split())
if a==b:
    print(a+b + c*2)
else:
    print(min(a,b)*2 + 1+ c*2)