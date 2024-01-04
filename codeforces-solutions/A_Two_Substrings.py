from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())


def solve():
    word = ST()
    temp = word
    if "AB" in word:
        word = word.replace("AB","XX",1)
        if "BA" in word:
            return "YES"
        
    if "BA" in temp:
        temp = temp.replace("BA","XX",1)
        if "AB" in temp:
            return "YES"
        
    return "NO"
       
T = 1
# T = I()
for _ in range(T):
    print(solve())