from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))


def checker(seen,nums1,nums2,beg,end):
    ans = [beg,beg]
    dif = 0
    left = beg

    for ind in range(beg,end):
        if nums1[ind] not in seen:
            if dif < ind-left-1:
                ans = [left,ind-1]
                dif = ind-left-1
            left = ind+1
        
        seen[nums2[ind]] -= 1
        if seen[nums2[ind]] == 0:
            seen.pop(nums2[ind])
    return ans

t = I()
for _ in range(t):
    n = I()
    nums1 = IL()
    nums2 = IL()
    beg = 0
    ans = [0,0]
    seen = defaultdict(int)
    seen[nums2[0]] = 1
    for end in range(1,n):
        while end < n-1 and nums2[end] < nums2[end-1]:
            
        if nums2[end] < nums2[end-1]:
            res = checker(seen,nums1,nums2,beg,end)
            if res[1]-res[0] > ans[1]-ans[0]:
                ans = res
            beg = end
        seen[nums2[end]] += 1
    print(ans[0]+1,ans[1]+1)