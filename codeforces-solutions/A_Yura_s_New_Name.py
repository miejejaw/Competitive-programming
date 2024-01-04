from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    name = ST()
    beg = 0
    n = len(name)
    if n == 1 and name[0] == "^":
        print(1)
        continue
    ans = 0
    while beg < n:
        while beg < n and name[beg] == "^":
            beg += 1

        if beg == 0:
            ans += 1
            
        temp = 0
        while beg < n and name[beg] == "_":
            temp += 1
            beg += 1
            
        if temp and beg == n:
            ans += temp
        elif temp: 
            ans += temp-1
    print(ans)
    