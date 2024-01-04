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
    
    n = I()
    count = n//2 

    if n > 2: count += 1
    for num in range(9,n+1,6):  
        if num%2 != 0:
            count += 1
    
    for num in range(5,n+1,5):  
        if num%2!=0 and num%3 != 0:
            count += 1
            
    for num in range(7,n+1,7):  
        if num%2 != 0 and num%3!=0 and num%5!=0:
            count += 1
     
    print(n-count)

T = 1
for _ in range(T):
    solve()
    
    
    # if n > 2: count += 1
    # if n > 8: count += math.ceil((n-9)/6) + 1

    # if n > 24:
    #     temp = (n//5)/2
    #     count += (temp//3) * 2
    #     if temp%3 > 1: count += 1