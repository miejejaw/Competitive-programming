from itertools import accumulate
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    num = I()
    ans = 0
    if num > 1:
        ans = round(math.sqrt(num-1))
    print(ans)
        
    