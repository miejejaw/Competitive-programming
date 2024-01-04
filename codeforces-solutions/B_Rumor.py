from itertools import accumulate
from collections import defaultdict
from heapq import heapify,heappop,heappush
from queue import deque

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,m = IL()
c = IL()
friends = defaultdict(list)
seen = set()
for _ in range(m):
    f1,f2 = IL()
    f1 -= 1
    f2 -= 1
    if f1 in seen:
        seen.remove(f1)
    if f1 not in friends:
        seen.add(f1)
        
    if f2 in seen:
        seen.remove(f2)
    if f2 not in friends:
        seen.add(f2)
    
    friends[f1].append(f2)
    friends[f2].append(f1)
    
visited = set()
total = sum(c)
for num in seen:
    if num not in visited: 
        queue = deque([num])
        s = set({num})
        total -= c[num]
        temp = c[num]
        while queue:
            x = queue.popleft()
            for a in friends[x]:
                if a not in s:
                    s.add(a)
                    queue.append(a)
                    visited.add(a)
                    temp = min(temp,c[a])
                    total -= c[a]
                    
        total += temp
                                             
print(total)
        
    
    

    
