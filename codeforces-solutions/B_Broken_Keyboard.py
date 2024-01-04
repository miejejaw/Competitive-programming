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
    ans = set()
    beg = 0
    for end in range(1,n):
        if word[end] != word[beg]:
            if (end-beg)%2 == 1:
                ans.add(word[beg])
            beg = end
            
    if (n-beg)%2 == 1:
        ans.add(word[beg])
        
    print("".join(sorted(ans)))
        

# T = 1
T = I()
for _ in range(T):
    solve()