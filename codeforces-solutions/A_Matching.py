from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    num = ST()
    if num[0] == "0":
        print(0)
        continue
    
    n = len(num)
    total = 1
    for ind in range(n):
        if num[ind] == "?":
            if ind == 0:
                total *= 9
            else:
                total *= 10
    print(total)