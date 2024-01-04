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
    l,r = IL()
    ans = 0
    while l or r:
        temp = abs(l%10 - r%10)
        l //= 10
        r //= 10
        if r > l: ans += 9
        else: ans += temp
        
    print(ans)
        
        