from heapq import heappush,heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        length = len(heights)
        heap = []
        ind = 1

        while ind<length and ladders:
            if heights[ind] > heights[ind-1]:
                heappush(heap , heights[ind]-heights[ind-1])
                ladders -= 1
            ind += 1

        while ind<length and bricks:
            gap = heights[ind] - heights[ind-1]
            if gap > 0: 
                temp = heappop(heap) if heap else float("inf")             
                if temp < gap and temp <= bricks:
                    bricks -= temp
                    heappush(heap,gap)
                elif gap <= bricks:
                    bricks -= gap
                    heappush(heap,temp)
                else:
                    break 
            ind += 1
            
        while ind < length and  heights[ind] <= heights[ind-1]:
            ind += 1

        return ind - 1