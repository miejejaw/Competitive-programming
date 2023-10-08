class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = defaultdict(list)
        for idx,(a,b) in enumerate(edges):
            adj[a].append((b,idx))
            adj[b].append((a,idx))
        
        heap = [(-1,start_node)]
        visited = set()

        while heap:
            w,curr = heappop(heap)
            if curr in visited: continue
            if curr == end_node: return -w
            visited.add(curr)

            for node,idx in adj[curr]:
                if node not in visited:
                    heappush(heap,(w*succProb[idx],node))
        
        return 0

