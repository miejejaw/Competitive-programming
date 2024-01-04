# import sys
# sys.setrecursionlimit(10**8)
from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,k = IL()
cats = IL()
paths = defaultdict(list)
for _ in range(n-1):
    parent,child = IL()
    paths[parent].append(child)
    paths[child].append(parent)
    
ans = 0
def dfs(vertex,noCats):
    global k,ans
    if not paths[vertex]:
        ans += 1
        return
    
    while paths[vertex]:
        v = paths[vertex].pop()
        paths[v].remove(vertex)
        if cats[v-1] == 0: 
            dfs(v, 0)       
        elif noCats < k:
            dfs(v, noCats+1)
            
if cats[0] == 1:           
    dfs(1,1)
elif 1 in paths:
    dfs(1,0)
print(ans)   
    