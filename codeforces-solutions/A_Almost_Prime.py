from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()+1
count = 0
for num in range(6,n):
    d = 2
    seen = set()
    while d*d <= num:
        while num%d == 0:
            seen.add(d)
            num //= d
        d += 1
    if num > 1:
        seen.add(num)
    if len(seen) == 2:
        count += 1
   
print(count)