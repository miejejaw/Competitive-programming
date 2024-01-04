from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

ak = input().split()
be = input().split()

a = 0
b = 0
b_len,a_len = len(be),len(ak)

while a<a_len and b<b_len:
    if ak[a] != ak[b]:
        if ak[a][0]=="-" and be[b][0] != "-":
            b += 1
        elif ak[a][0]!="-" and be[b][0] == "-":
            a += 1
        else:
            print("NO")
            exit()
            
            

            