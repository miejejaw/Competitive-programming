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
    ind = nums.index(min(nums))
    ans = max(nums)
    
    for ind in range(n):
        for i in range(ind+1,n):
            ans = min(ans,nums[i]&nums[ind])
        
    print(ans)