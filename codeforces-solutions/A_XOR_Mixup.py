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
    for ind in range(n):
        num = 0
        for i in range(n):
            if i != ind:
                num ^= nums[i]
                
        if num == nums[ind]:
            print(num)
            break