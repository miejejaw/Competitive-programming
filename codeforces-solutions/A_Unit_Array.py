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
    neg = pos = 0
    for num in nums:
        if num < 0: neg += 1
        else: pos += 1
        
    temp = 0
    if neg > pos: 
        temp = math.ceil((neg-pos)/2)
        pos += temp
        neg -= temp
        
    if neg%2 == 1: 
        temp += 1
        
    print(temp)
    