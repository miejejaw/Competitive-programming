from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    
    num1 = 1
    while not num1 & n:
        num1 <<= 1
        
    if n == num1:   
        num2 = 1
        while num2 & n:
            num2 <<= 1
        num1 += num2
        
    print(num1)