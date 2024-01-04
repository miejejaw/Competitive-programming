from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    ans = []
    if n == 1:
        ans = [1]
    elif n%2:
        ans = [-1]
    else:
        for i in range(2,n+2,2):
            ans.append(i)
            ans.append(i-1) 
    print(*ans)