class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Use a heap to maintian the top k elements
        first build a k size heap of the first kelements
        then, the kth largest seen so far will always be at the top of the min-heap
        move through the rest of the elements and if the current item is bigger than then min in heap
            pop the top element off the heap, and add the current item
        once you are through all the items, the top item will be the kth smallest item in the list
            and the k-1 bigger items will all be below it in the heap
        '''
        import heapq
        k_large = [] #heap
        for i, item in enumerate(nums):
            # build heap out of the first k items
            if i < k:
                heappush(k_large, item)
            # if the cur item is bigger than the smallest in the heap pop smallest and add new one
            else:
                if item > k_large[0]:
                    heapq.heappop(k_large)
                    heapq.heappush(k_large, item)
        # return min of the heap
        return k_large[0]

        
