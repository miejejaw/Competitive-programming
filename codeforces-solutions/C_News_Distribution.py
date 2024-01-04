from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(1,n+1)}
        self.size = {i:1 for i in range(1,n+1)}
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a]) 
        return self.root[a]

    def union(self, nums):
        
        a = self.find(nums[0])
        for num in nums:
            b = self.find(num)
            if a > b:
                a = b
        
        for ind in range(len(nums)):
            b = self.find(nums[ind])
            self.root[b] = a
            if b != a:
                self.size[a] += self.size[b]
            
    def get(self,n):
        res = [0]*n
        for ind in range(n):
            b = self.find(ind+1)
            res[ind] = self.size[b]
        return res
        

n,m = IL()
unionFind = UnionFind(n)
for _ in range(m):
    _len,*nums = IL()
    if _len > 0:
        unionFind.union(nums)
print(*unionFind.get(n))
    