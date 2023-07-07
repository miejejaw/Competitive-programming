from heapq import heappush,heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        heap,length = [],len(tasks)
        arr = [ (enq,pro,ind)for ind,(enq,pro) in enumerate(tasks)]
        arr.sort()
        
        ans = []
        ind = totalTime = 0

        while ind < length:
            if not heap and totalTime < arr[ind][0]:
                totalTime = arr[ind][0]

            while ind<length and arr[ind][0] <= totalTime:
                _,proTime,idx = arr[ind]
                heappush(heap,(proTime,idx))
                ind += 1

            proTime,idx = heappop(heap)
            ans.append(idx)
            totalTime += proTime

        while heap:
            _,idx = heappop(heap)
            ans.append(idx)

        return ans
        
        
    
