from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))


t = I()
for _ in range(t):
    n,x = IL()
    nums = ILS() 
    total = 0
    prev = 1
    for num in nums:
        if num <= x:
            total -= num
            total += (num-prev)*(num+prev-1)//2
            prev = num+1
            
    if prev <= x:
        total += (x-prev+1)*(prev+x)//2
        
    print(total)