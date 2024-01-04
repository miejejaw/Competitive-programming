import itertools
import collections
n,a,b = map(int,input().split())
nums = list(map(int,input().split()))
nums = list(itertools.accumulate(nums))
dic = collections.defaultdict(int)
dic[0] = 1
beg = 0
end = 0
res = 0
for end in range(n):
    if nums[end]
               
print(res)