from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    a,b,c,d = IL()
    ans = -1
    if d >= b:
        temp = d - b
        a += temp
        if a >= c:
            ans = temp + abs(a-c)

    print(ans)
    