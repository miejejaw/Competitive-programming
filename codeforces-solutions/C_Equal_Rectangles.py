from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    nums = ILS()
    temp = nums[0]*nums[-1]
    beg = 0
    end = n*4 - 1
    ans = "YES"
    while beg < end:
        if nums[beg]*nums[end] != temp or nums[end]!=nums[end-1] or nums[beg]!=nums[beg+1]:
            ans = "NO"
            break
        beg += 2
        end -= 2
    
    print(ans)
