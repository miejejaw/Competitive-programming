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
    
    grid = []
    for _ in range(n):
        grid.append(ST())
    
    count = 0
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            char = max(grid[i][j],grid[n - j - 1][i],grid[n - i - 1][n - j - 1],grid[j][n - i - 1])
            char = ord(char)
            count += char - ord(grid[i][j])
            count += char - ord(grid[n - j - 1][i] )
            count += char - ord(grid[n - i - 1][n - j - 1])
            count += char - ord(grid[j][n - i - 1])
    
    print(count)



# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())