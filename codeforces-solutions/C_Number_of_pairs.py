boys = int(input())
boy = list(map(int,input().split()))
girls = int(input())
girl = list(map(int,input().split()))
boy.sort()
girl.sort()

b,g = 0,0
res = 0
while b<boys and g<girls:
    if abs(boy[b]-girl[g]) < 2:
        res += 1
        g += 1
        b += 1
    elif boy[b]>girl[g]:
        g += 1
    else:
        b += 1
print(res)

