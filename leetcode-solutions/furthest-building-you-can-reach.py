from heapq import heappush,heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        length = len(heights)
        heap,ind = [],1

        while ind < length:
            gap = heights[ind] - heights[ind-1]
            if gap > 0:
                if ladders:
                    heappush(heap,gap)
                    ladders -= 1           
                elif heap and heap[0] < gap and heap[0] <= bricks:
                    bricks -= heappop(heap)
                    heappush(heap,gap)
                elif gap <= bricks:
                    bricks -= gap
                else: 
                    break
                
            ind += 1
            
        return ind - 1