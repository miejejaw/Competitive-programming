class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for a,b,price in flights:
            graph[a].append((b,price))

        heap = deque([(0, src)])
        distances = [float("inf")] * n
        ans = float("inf")

        while k+1:
            size = len(heap)
            for _ in range(size):
                current_distance, current_node = heap.popleft()
                

                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heap.append((distance, neighbor))

                        if neighbor == dst: 
                            ans = min(ans,distance)

            
            k -= 1
        
        return -1 if ans == float("inf") else ans