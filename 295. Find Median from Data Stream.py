import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:
        #adding the number 
        if not self.maxheap and not self.minheap:
            heapq.heappush(self.maxheap,-1*num)
        elif self.maxheap and not self.minheap:
            heapq.heappush(self.maxheap,-1*num)
        elif self.minheap[0] >= num:
            heapq.heappush(self.maxheap,-1*num)
        else: 
            heapq.heappush(self.minheap,num)
        
        #Mainining the invariant if need be 
        if len(self.minheap) - len(self.maxheap) == 2: 
            a = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-1*a)
        elif len(self.maxheap) - len(self.minheap) == 2: 
            a = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-1*a)
        

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0])/2
        elif len(self.maxheap) > len(self.minheap):
            return -1*self.maxheap[0]
        else: 
            return self.minheap[0]



