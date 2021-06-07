class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.heap = []
        self.k = k
        for i, num in enumerate(nums):
            if i < k:
                heapq.heappush(self.heap, num)
            elif num >= self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
