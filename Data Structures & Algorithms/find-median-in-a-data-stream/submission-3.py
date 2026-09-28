class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            t1 = -heapq.heappop(self.maxHeap)
            t2 = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, t1)
            heapq.heappush(self.maxHeap, -t2)
            

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]
        
        