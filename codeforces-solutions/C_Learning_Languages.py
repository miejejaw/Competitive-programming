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
    n,m = IL()
    for _ in range(n):
        emp,*lang = IL()
        
        
    
    
    
    print()
         
T = 1
# T = I()
for _ in range(T):
    solve()
    

class Union:
    def __init__(self, m):
        self.nums = [i for i in range(m+1)]
        self.size = [1 for i in range(m+1)]
    
    def find(self,a):
        if a != self.nums[a]:
            self.nums[a] = self.find(self.nums[a])
        return self.nums[a]
    
    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        
        if a == b: return 
        
        if b < a:
            a,b = b,a
        
        self.nums[b] = a
        self.size[a] += self.size[b]