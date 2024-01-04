from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

def trav(nums,left,right):
    if left == right:
        return 0
    mid = left + (right-left)//2
    count = 0
    count += trav(nums,left,mid)
    count += trav(nums,mid+1,right)
    if nums[left] > nums[mid+1]:
        count += 1
        rotate(nums,left,mid+1)
    return count

def rotate(nums,left,right):
    gap = right - left
    for ind in range(left,right):
        nums[ind],nums[ind+gap] = nums[ind+gap],nums[ind]
    
    

t = I()
for _  in range(t):
    m = I()
    nums = IL()
    count = trav(nums,0,m-1)
    for ind in range(0,m):
        if nums[ind] != ind+1:
            count = -1
            break
    
    print(count)
    # 2426