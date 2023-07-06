from heapq import heappush,heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        rows,cols = len(matrix),len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                heappush(heap,-matrix[row][col])
                if k == 0: heappop(heap)
                else: k -= 1
            
        return -heap[0]