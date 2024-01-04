from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict,Counter
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def solve():
    word1,word2 = ST().split()
    word2 = Counter(word2)
    count = 0
    for ch in word1:
        if word2[ch] == 0:
            break
        
        word2[ch] -= 1
        count += 1
    
    print(count)

# T = 1
T = I()
for _ in range(T):
    solve()