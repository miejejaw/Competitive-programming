t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if c == 0:
        print(min(a,b)*4)
    elif b>=a:
        print(a*4)
    else:
        temp = min(a*c+(4-c)*b, (4+c)*b)
        print(temp)
        