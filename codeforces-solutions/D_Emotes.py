from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,m,k = IL()
nums = ILS()

b = m//(k+1)
ans = nums[-2]*b

b = m%(k+1) + b*k
ans += nums[-1]*b          
print(ans)