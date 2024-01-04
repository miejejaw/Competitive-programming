from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
nums = IL()
ans = [0]*2
a,b = nums[0],0 
ans[0] = 1 
beg,end = 1,n-1

while beg <= end:
    
    if a <= b:
        ans[0] += 1
        a += nums[beg]
        beg += 1
    else:
        ans[1] += 1
        b += nums[end]
        end -= 1 
print(*ans)