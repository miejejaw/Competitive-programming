import collections
n,k = map(int,input().split())
nums = list(map(int,input().split()))
beg = 0
seen = collections.defaultdict(int)
left = 0
right = 0
ans = 0
for end in range(n):
    while len(seen) == k and nums[end] not in seen:
        seen[nums[beg]] -= 1 
        if seen[nums[beg]] == 0:
            seen.pop(nums[beg]) 
        beg += 1
    seen[nums[end]] += 1
    if len(seen) <= k:
        if ans < end - beg +1:
            left = beg + 1
            right = end +1
            ans = end-beg+1
        
print(left,right)