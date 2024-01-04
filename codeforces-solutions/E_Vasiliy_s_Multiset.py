from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input().split())

class Node:
    def __init__(self):
        self.dd = [None,None]
        self.cc = [0,0]
        
class Trie:
    def __init__(self):
        self.root = Node()
        self.length = 31
    
    def insert(self, s, l):
        
        curr = self.root
        idx = 0
        for _ in range(31-l):
            if not curr.dd[0]:
                curr.dd[0] = Node()
            curr.cc[0] += 1
            curr = curr.dd[0]
            
        for b in s:
            b = int(b)
            if not curr.dd[b]:
                curr.dd[b] = Node()
                
            curr.cc[b] += 1
            curr = curr.dd[b]
    
    def remove(self, s, l):
        
        curr = self.root
        idx = 0
        for _ in range(self.length-l):
            if not curr.dd[0]:
                curr.dd[0] = Node()
            curr.cc[0] -= 1
            curr = curr.dd[0]
            
        for b in s:
            b = int(b)
            if not curr.dd[b]:
                curr.dd[b] = Node()
                
            curr.cc[b] -= 1
            curr = curr.dd[b]
    
    
    def trav(self, s, l):
        
        curr = self.root
        p = 2**30
        res = 0
        for _ in range(31-l):
            if curr.dd[1]:
                res += p
                curr = curr.dd[1]
            else:
                curr = curr.dd[0]
            p //= 2
 
        for b in s:
            if b == "1":
                if curr.dd[0] and curr.cc[0]:
                    res += p
                    curr = curr.dd[0]
                else:
                    curr = curr.dd[1]
            else:
                if curr.dd[1] and curr.cc[1]:
                    res += p
                    curr = curr.dd[1]
                else:
                    curr = curr.dd[0]
                    
            p //= 2
        return res  
        
def solve():
    n = I()
    trie = Trie()
    
    for _ in range(n):
        op,num = STL()
        bb = bin(int(num))[2:]
        
        if op == "+":
            trie.insert(bb,len(bb))
        elif op == "-":
            trie.remove(bb,len(bb))
        else:
            ans = trie.trav(bb,len(bb))
            print(ans)


T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())