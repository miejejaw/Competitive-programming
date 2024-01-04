from itertools import accumulate
from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
nums = defaultdict(list)
for i in range(1,n+1):
   b = I()
   if b != -1:
    nums[b].append(i)
 
ans = 1  
def dfs(emp,depth):
    global ans
    ans = max(ans,depth)
    if emp in nums:
        for i in nums[emp]:
            dfs(i,depth+1)

for emp in nums:
    dfs(emp,1)
print(ans)
