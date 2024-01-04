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
    step = ST()
    
    count = 0
    non_des = None
    ans = "YES"
    
    for op in step:
        if op == "+":
            count += 1
        elif op == "-":
            count -= 1
        elif op == "1":
            if non_des == False or (non_des==None and count==0): 
                ans = "NO"
                break
            if count > 1:
                non_des = True
        else:
            if non_des == True or (non_des==None and count<=1):
                ans = "NO"
                break
            if count > 1:
                non_des = False
        
        if count<2:
            non_des = None
                 
    print(ans)
    
# T = 1
T = I()
for _ in range(T):
    solve()