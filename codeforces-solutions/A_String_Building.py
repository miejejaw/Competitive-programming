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
    n = len(word)
    beg,end = 0,0
    
    while end<n:
        while end<n and word[end]==word[beg]:
            end += 1
        
        if (end-beg) == 1 or end+1 == n:
            print("NO")
            return
        
        beg = end
        end += 1
        
    print("YES")
       
# T = 1
T = I()
for _ in range(T):
    solve()