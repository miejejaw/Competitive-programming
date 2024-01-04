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
    n,c = IL()
    nums = IL()
    count = 0
    dic = defaultdict(int)
    for num in nums:
        dic[num] += 1
    for num,freq in dic.items():
        if freq>c:
            count += c
        else:
            count += freq
    print(count)