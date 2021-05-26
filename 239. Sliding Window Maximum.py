from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Use a deque (double ended queue) to keep track of max elements in the window [O(1) insert/delete from either end]
        first element in the queue represents the index for largest element in the current window
        as we extend the window, from right to left remove elements that are less than this new value.
            These are values that will never be maxes as they are smaller than the more recent element added
        Then remove the first item in the queue if it is at the index that just fell out of the sliding window
        max for this window is then just the first element in the queue

        '''
        maxes = []
        max_q = deque()
        for i, n in enumerate(nums):
            while max_q and nums[max_q[-1]] < n:
                max_q.pop()
            max_q.append(i)
            if max_q[0] == i - k:
                max_q.popleft()
            if i >= k - 1:
                maxes.append(nums[max_q[0]])
        return maxes


            
