from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    nums = IL()
    one = nums.index(1)+1
    two = nums.index(2)+1
    n = nums.index(n)+1
    
    a = b = 0
    if two<one<n:
        print(one,n)
    elif one<two<n:
        print(two,n)
    elif n<two<one:
        print(n,two)
    elif n<one<two:
        print(n,one)
    else:
        print(one,one)