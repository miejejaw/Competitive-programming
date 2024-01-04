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
    s = STL()
    
    if n%2 == 1: 
        print(-1)
        return 
    
    left,right = 0,n
    count = 0
    queue = deque(s)
    
    ans = []
    while queue:
        if queue[0] != queue[-1]:
            queue.popleft()
            queue.pop()
            left += 1
            right -= 1
        else:
            if queue[0] == "0":
                queue.append("0")
                queue.append("1")
                ans.append(right)
            else:
                queue.appendleft("1")
                queue.appendleft("0")
                ans.append(left)
                
            right += 2
            count += 1
        
        if count > 300: break
    
    else:
        print(count)
        print(*ans)
        return
    
    print(-1)        

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())