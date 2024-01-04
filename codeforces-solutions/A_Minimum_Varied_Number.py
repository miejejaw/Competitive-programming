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
    num = I()

    res = ""
    n = 9
    while num and n <= num:
        res = str(n)+res
        num -= n
        n -= 1
    if num:
        res = str(num)+res
    print(res)