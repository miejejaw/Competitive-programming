t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    temp = set(arr)
    if len(arr)==len(temp):
        print("YES")
    else:
        print("NO")
    