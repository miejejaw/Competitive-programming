import math
def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

a,b = IL()
res = [1]
d = 2
while d*d <= a or d*d <= b:
    x,y = 0,0
    while a%d==0 or b%d==0:
        if a%d==0:
            x += 1
            a //= d
        if b%d==0:
            y += 1
            b //= d
    
    if x>0 and y>0:
        x = min(x,y)
        _len = len(res)
        for i in range(_len):
            for j in range(1,x+1):
                res.append(res[i]*(d**j))
    d += 1

if a == b:
    _len = len(res)
    for i in range(_len):
        res.append(res[i]*a)
        
n = I()
res.sort()
def binary_search_max(array, a, b):
    if not array or b < array[0] or array[-1] < a:
        return -1
    left = 0
    right = len(array) - 1
    possible = -1
    while left <= right:
        mid = (left + right) // 2
        if a <= array[mid] <= b:
            possible = array[mid]
            left = mid + 1
        elif array[mid] < a:
            left = mid + 1
        else:
            right = mid - 1
    return possible
for _ in range(n):
    a,b = IL()
    
    print(binary_search_max(res,a,b))
