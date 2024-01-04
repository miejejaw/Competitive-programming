from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,t = IL()
nums = IL()
ind = 0
while ind < n-1 and ind+1 < t:
    ind += nums[ind]
    
ans = "NO"   
if t == ind+1:
    ans = "YES"
    
print(ans)