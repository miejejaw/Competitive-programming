from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n,k = IL()
    p = 0
    num = 0
    for bit in reversed(bin(k)):
        if bit == "1":
            num += n**p
        p += 1
    print(num % (10**9+7))
    

