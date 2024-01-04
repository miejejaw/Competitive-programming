from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

x = I()
count = 0
num = 0
while x:
    temp = 1
    while temp < x:
        temp <<= 1
    if temp > x:
        temp >>= 1
    count += 1
    x -= temp
    num += temp
    
print(count)
