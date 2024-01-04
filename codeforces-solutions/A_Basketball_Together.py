from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,d = IL()
nums = ILS()
ans = 0
end = n-1
beg = 0
total = nums[end]
while beg <= end:
    if total <= d:
        total += nums[end]
        beg += 1
    else:
        ans += 1
        end -= 1
        total = nums[end]
        
print(ans)