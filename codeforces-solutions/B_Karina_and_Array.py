from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    nums = ILS()
    num1 = nums[0]*nums[1]
    num2 = nums[-1]*nums[-2]
    print(max(num1,num2))