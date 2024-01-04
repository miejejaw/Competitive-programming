from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

def check(nums,k,h,n):
    total = k
    for ind in range(n-1):
        total += min(k, nums[ind+1] - nums[ind])
    return total >= h


t = I()
for _ in range(t):
    n,h = IL()
    nums = IL()

    left = 0
    right = h
    while left < right:
        mid = left + (right - left)//2
        if check(nums,mid,h,n):
            right = mid
        else:
            left = mid + 1
    print(left)

