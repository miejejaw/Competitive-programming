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
    x = 0
    for num in nums:
        x ^= num
    
    t = 0
    for num in nums:
        t ^= x^num
            
    if t == 0:
        print(x)
    else:
        print(-1)
        
