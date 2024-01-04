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
    ans = 0
    count = nums.count(1)
    ans = count//2 + count%2 + n-count    
    print(ans)