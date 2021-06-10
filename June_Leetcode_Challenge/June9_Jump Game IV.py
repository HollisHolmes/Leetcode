class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        '''
        This one is really cool, classic DP where we take cost + max over last values we can jump from
        The first key insight is to use DP, but the second is how to track the max over prev values
        We don't want to have to take maxes over the last K elements everytime, so how do we track it.
        Using a queue, tracking the indices.
        Popleft of the queue if the index is falling out of the sliding window.
        The current max is left, so use nums[q[0]]
        Now we add the current value, if cur value is bigger than some values already in the window, then
            those values are useless, because the current value is bigger and will outlast them so they
                will never be used again, so pop them
                    while DP[i] > DP[q[-1]]: q.pop()   then add the current to the end of the queue and repeat
        Can modify nums in place to save space.
        '''
        DP = [0 for _ in nums]
        q = deque()
        for i, num in enumerate(nums):
            # base case hase no choices to make
            if i == 0:
                q.append(0)
                DP[0] = nums[0]
                continue
            # remove index that is falling out to the left of the window
            if q[0] == i - k -1:
                q.popleft()
            # add cur num to the max in the window, at the index held at the left of the queue
            DP[i] = DP[q[0]] + nums[i]
            # remove values from right to left that are less than the current value
            while q and DP[q[-1]] < DP[i]:
                q.pop()
            # add the current item
            q.append(i)
        return DP[-1]
