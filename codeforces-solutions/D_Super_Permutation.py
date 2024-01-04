from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    if n == 1:
        print(1)
    elif n%2 == 1:
        print(-1)
    else:
        nums = [n]
        i,j = 2,n-1
        while j > 1:
            nums.append(j)
            nums.append(i)
            i += 2
            j -= 2
            
        print(*nums,1)
        