from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
nums = IL()
ans = "NO"

for ind in range(n):
    if ind+1 != nums[ind]:
        st = set({ind+1})
        i = ind
        while nums[i] not in st and i+1 != nums[i]:
            st.add(nums[i])
            i = nums[i]-1
            
        if len(st) == 3 and nums[i] == ind+1:
            ans = "YES"
            break
    
print(ans)
    
