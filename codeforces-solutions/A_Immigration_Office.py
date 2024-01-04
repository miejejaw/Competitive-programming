n = int(input())
names = list(map(str,input().split()))
q = int(input())
for _ in range(q):
    if not names:
        print(0)
        continue
    name = input()
    ans = len(names)
    for ind in range(len(names)):
        if name <= names[ind]:
            ans = ind
            break
    print(ans)
    