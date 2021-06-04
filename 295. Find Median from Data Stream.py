class MedianFinder:
    import heapq

    def __init__(self):
        """
        initialize your data structure here.
        """
        # heapq is a minheap, need to insert and get -ve elements for the maxheap
        self.small_heap = [] # smaller items, maxheap
        self.big_heap = [] # bigger items, minheap

    def addNum(self, num: int) -> None:
        if not self.big_heap:
            big_half = True
        else:
            # should this number go into the big heap
            big_half = num >= self.big_heap[0]
        if big_half:
            heapq.heappush(self.big_heap, num)
            if len(self.big_heap) >=  len(self.small_heap)+2:
                switch_element = heapq.heappop(self.big_heap)
                heapq.heappush(self.small_heap, -1*switch_element)

        else:
            heapq.heappush(self.small_heap, -1*num)
            if len(self.small_heap) >=  len(self.big_heap)+2:
                switch_element = -1 * heapq.heappop(self.small_heap)
                heapq.heappush(self.big_heap, switch_element)

    def findMedian(self) -> float:
        even = (len(self.small_heap) + len(self.big_heap)) % 2 == 0
        if even:
            return (-1 * self.small_heap[0] + self.big_heap[0])/2
        else:
            big_heap_bigger = len(self.big_heap)>len(self.small_heap)
            if big_heap_bigger:
                return self.big_heap[0]
            else:
                return -1 * self.small_heap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
