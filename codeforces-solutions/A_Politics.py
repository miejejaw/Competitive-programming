from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n,k = IL()
    nums = [ST() for _ in range(n)]
    arr = [i for i in range(n)]
    
    for ind in range(k):
        res = []
        s = nums[0][ind]
        for i in arr:
            if nums[i][ind] == s:
                res.append(i)
        arr = res
    print(len(arr))
