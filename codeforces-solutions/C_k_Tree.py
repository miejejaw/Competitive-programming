from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,k,d = IL()
dic = {0:(0,False)}

def t(n,k,d):
    if n in d: return d[n]
    res = 0
    for weight in range(1,k):
        if n-weight >= 0:
            res += t(n-weight,k,d)
    temp = False
    if n >= d:
        temp = True
    dic[n] = (res+1,temp)
    return dic[n]
        
    