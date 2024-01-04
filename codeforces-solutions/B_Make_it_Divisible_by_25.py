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
    nums = ST()[::-1]
    five,zero = False,False
    for i,num in enumerate(nums):
        if not five and num =="5":
            five = True
        elif not zero and num=="0":
            zero = True
            continue
            
        if five and (num =="2" or num=="7"):
            print(i-1)
            break
        elif zero and (num=="0" or num=="5"):
            print(i-1)
            break
