from collections import defaultdict
from queue import deque

def parallelCourses(n, prerequisites):
        
    adjList = defaultdict(list)
    indgree = [0]*(n+1)
    for u,v in prerequisites:
        adjList[u].append(v)
        indgree[v] += 1
    
    queue = deque()
    for node in range(1,n+1):
        if indgree[node] == 0:
            queue.append((node,1))
            
    ans = 0
    while queue:
        curr,time = queue.popleft()
        n -= 1
        ans = max(ans,time)
        time += 1
        for node in adjList[curr]:
            indgree[node] -= 1
            if indgree[node] == 0:
                queue.append((node,time))
        
    return ans if n == 0 else -1
