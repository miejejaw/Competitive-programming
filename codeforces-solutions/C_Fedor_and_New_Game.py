from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,m,k = IL()
nums = [I() for _ in range(m)]
m = I()
count = 0
for num in nums:
    num ^= m
    if bin(num).count("1") <= k:
        count += 1
        
print(count)