from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    nums = IL()
    seen = defaultdict(int)
    res = 0
    for num in nums:
        a = num.bit_length()
        if a in seen:
            res += seen[a]
        seen[a] += 1
        
    print(res)