from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

num1,num2 = IL()

if num1 == num2:
    print(num1)
else:
    print(1)