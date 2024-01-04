from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    a,b,c,d = sorted(map(int,ST()))

    ans = 4
    if a == b == c== d:
        ans = -1
    elif a == b == c or b == c== d:
        ans = 6
        
    print(ans)