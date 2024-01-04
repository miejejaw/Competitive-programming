from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,q = IL()
nums = IL()
arr = [0]*n
beg = 0
end = 0
num = 0
while end<n:
    while end+1<n and nums[end]>=nums[end+1]:
        end += 1
    if beg+2 <= end:
        num += 1
    
    end += 1   
    for i in range(beg,end):
        arr[i] = num
    
    beg = end
        
        
for _ in range(q):
    l,r = IL()
    m = r-l+1
    if m < 3:
        print(m)
    elif r+1<n and arr[r+1]>arr[r]:
        print(m-arr[r]+arr[l])
    else:
        print(m-arr[r]+arr[l]+1)
    