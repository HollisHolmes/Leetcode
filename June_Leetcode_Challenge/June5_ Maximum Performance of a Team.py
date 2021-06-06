class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        '''
        yooooo this is a DP knapsack problem
        '''
        from heapq import heapify,heappush,heappop
        heap=[]
        heapify(heap)
        result=0
        totalspeed=0

        pairs = list(zip(efficiency, speed))
        pairs.sort(key=lambda x:x[0], reverse=True)

        for eff , sp in pairs:
            heappush(heap,sp)
            totalspeed+=sp

            if len(heap)>k:
                totalspeed-=heappop(heap)

            result=max(result,totalspeed*(eff))


        return result%(10**9+7)
