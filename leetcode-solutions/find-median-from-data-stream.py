from heapq import heappush,heappop
class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.minLen = self.maxLen = 0

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap,num)
        num = heappop(self.maxHeap)
        heappush(self.minHeap,-num)
        if self.minLen != self.maxLen:
            heappush(self.maxHeap,-heappop(self.minHeap))
            self.maxLen += 1
        else:
            self.minLen += 1

    def findMedian(self) -> float:
        if self.minLen == self.maxLen:
            return (-self.minHeap[0]+self.maxHeap[0]) / 2
        return -self.minHeap[0]

