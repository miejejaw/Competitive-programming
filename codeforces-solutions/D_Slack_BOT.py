from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

class Node:
    def __init__(self):
        self.dd = [None]*26
        self.cc = [0]*26
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, s):
        
        curr = self.root
        for ch in s:
            idx = ord(ch)-97
            curr.cc[idx] += 1
            if not curr.dd[idx]:
                curr.dd[idx] = Node()
            curr = curr.dd[idx]
    
    def trav(self, s):
        
        count = 0
        curr = self.root
        for ch in s:
            idx = ord(ch)-97
            if curr.cc[idx] < 2:
                break
            count += 1
            curr = curr.dd[idx]
        return count      
    
def solve():
    n = I()
    arr = []
    trie = Trie()
    
    for _ in range(n):
        s = ST()
        arr.append(s)
        trie.insert(s)
    
    for s in arr:
        print(trie.trav(s))
    
    
T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())