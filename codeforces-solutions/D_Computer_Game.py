from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    row1 = ST()
    row2 = ST()
    ans = "YES"
    for ind in range(n):
        if row1[ind]=="1" and row2[ind]=="1":
            ans = "NO"
            break
    print(ans)