class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        dist = [float("inf")] * (n+1)
        dist[k] = 0

        for a,b,w in times:
            adj[a].append((b,w))
        
        heap = [k]

        while heap:
            u = heappop(heap)
            for v,w in adj[u]:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(heap,v)
                    
        ans = -1
        for idx in range(1,n+1):
            if dist[idx] == float("inf"): return -1
            if idx != k:
                ans = max(ans,dist[idx])

        return ans