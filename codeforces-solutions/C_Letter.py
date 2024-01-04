from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

word = ST()
length = len(word)
beg,end = 0,length-1

while beg<length and word[beg].isupper():
    beg += 1

while end>=0 and word[end].islower():
    end -= 1

if beg > end:
    print(0)
    exit()
    
end += 1
ans = 0
while beg < end:
    lower = upper = 0
    
    while beg<end and word[beg].islower():
        beg += 1
        lower += 1
        
    while beg<end and word[beg].isupper():
        beg += 1
        upper += 1
    
    ans += min(upper,lower)     
print(ans)
    