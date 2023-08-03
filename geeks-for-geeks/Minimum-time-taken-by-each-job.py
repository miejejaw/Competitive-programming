from typing import List
from collections import defaultdict
from queue import deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        
        adjList = defaultdict(list)
        indgree = [0]*(n+1)
        for u,v in edges:
            adjList[u].append(v)
            indgree[v] += 1
        
        queue = deque()
        for node in range(1,n+1):
            if indgree[node] == 0:
                queue.append((node,1))
                
        res = [0]*n
        while queue:
            curr,time = queue.popleft()
            res[curr-1] = time
            time += 1
            for node in adjList[curr]:
                indgree[node] -= 1
                if indgree[node] == 0:
                    queue.append((node,time))
        
        return res
