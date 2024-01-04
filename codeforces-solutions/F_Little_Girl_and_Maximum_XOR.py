from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

def solve(num):
    p = 0
    res = 0
    while num:
        res += 2**p
        p += 1
        num >>= 1
    return res
    
a,b = ILS()
if a.bit_length() != b.bit_length():
    print(solve(b))
else:
    a ^= b
    print(solve(a))









        
    


