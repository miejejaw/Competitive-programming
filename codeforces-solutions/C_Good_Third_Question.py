from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,m = IL()
nums = ILS()
half = m//2
for _ in range(n):
    num = I()
    
    left = 0
    right = m - 1
    
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] >= num:
            right = mid
        else:
            left = mid + 1
    
    if m > m-left > half:
        print("YES")
    else:
        print("NO")