from heapq import heappush,heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        heap,length = [],len(tasks)
        arr = []
        for ind in range(length):
            arr.append(tasks[ind]+[ind])

        arr.sort()
        ans = []
        ind = totalTime = 0

        while ind < length:
            if not heap:
                totalTime = arr[ind][0]
                while ind<length and totalTime == arr[ind][0]:
                    _,pro,idx = arr[ind]
                    heappush(heap,(pro,idx))
                    ind += 1

            time,idx = heappop(heap)
            ans.append(idx)
            totalTime += time
            while ind<length and arr[ind][0] <= totalTime:
                _,pro,idx = arr[ind]
                heappush(heap,(pro,idx))
                ind += 1

        while heap:
            _,idx = heappop(heap)
            ans.append(idx)

        return ans
        
        
    
