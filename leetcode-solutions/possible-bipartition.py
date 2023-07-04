class Solution:
    def unionFind(self, arr, ind):
        if arr[ind] == ind:
            return ind
        arr[ind] = self.unionFind(arr,arr[ind])
        return arr[ind]

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for node1,node2 in dislikes:
            adj[node1-1].append(node2-1)
            adj[node2-1].append(node1-1)
            
        color = [0]*n
        queue = deque()
        visited = set()
                
        for ind in range(n):
            if ind in visited: continue
            queue.append(ind)
            visited.add(ind)
            color[ind] = 1
            while queue:
                curr = queue.popleft()
                for node in adj[curr]:
                    if node in visited:
                        if color[curr] == color[node]:
                            return False
                        else:
                            continue
                    queue.append(node)
                    visited.add(node)
                    color[node] = 1 if color[curr] == 2 else 2      
        
        return True