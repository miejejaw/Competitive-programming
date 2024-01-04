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
    i = 0
    temp = 0
    for ind in range(n):
        num = nums[ind]
        while num %2 == 0:
            num //= 2
            
        if num > temp:
            i = ind
            temp = num
               
    for ind in range(n):
        if ind != i:
            while nums[ind]%2 == 0:
                nums[i] *= 2
                nums[ind] //= 2 
    
    print(sum(nums))   
