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
    
    points = 0
    for row in range(10):
        rows = ST()
        for col in range(10):
            temp = points
            if rows[col] == "X":
                if row<5 and (col<row or 10-col <= row):
                    points += col+1 if col<5 else 5 - col%5
                elif row>4 and (col < 4-row%5 or col>row):
                    points += col+1 if col<5 else 5 - col%5
                else:
                    points += row+1 if row<5 else 5 - row%5
                    
    print(points)
    
    
        
# T = 1
T = I()
for _ in range(T):
    solve()