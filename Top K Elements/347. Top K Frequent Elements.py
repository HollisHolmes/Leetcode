class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        First count the elemets
        Then lenght k priority queue minheap with frequency as the key
        Return the items in the queue afterwards
        '''
        import heapq
        def count_items(nums):
            '''
            Return a dictionary where values are the frequency of the key in input list
            '''
            count = {}
            for num in nums:
                if num not in count:
                    count[num] = 0
                count[num] += 1
            return count

        def find_top_k(count):
            '''
            Maintain a minheap of the k highest frequencies in input count dictionary
            Return the final minheap of k highest frequency items
            '''
            k_heap = []
            for i, (item, freq) in enumerate(count.items()):
                if i < k:
                    heapq.heappush(k_heap, (freq, item))
                elif freq > k_heap[0][0]:
                    heapq.heappop(k_heap)
                    heapq.heappush(k_heap, (freq, item))
            return k_heap

        count = count_items(nums)
        top_k = find_top_k(count)
        return [item[1] for item in top_k]
