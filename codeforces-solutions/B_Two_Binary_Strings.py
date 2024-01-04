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
    num1 = ST()
    num2 = ST()
    
    n = len(num1)
    for ind in range(1,n):
        if num1[ind]==num2[ind]=="1":
             if num1[ind-1]==num2[ind-1]=="0":
                 print("YES")
                 return
                
    print("NO")
    
# T = 1
T = I()
for _ in range(T):
    solve()