class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Loop through the items once, where the thing being looped is the end of a sliding window.
        Track the current minimum length of the sliding window, comparing to prev max at each iter.
        If sum of window is >= target,
            Then shrink window from the left until it is no longer larger than target
            Smallest larger is one more than what the window ends up (also check start <= end)
        Else
            we need to extend window, so continue
        return max
        '''
        min_window_len = float('inf')
        start = 0
        window_sum = 0
        for end in range(len(nums)):
            window_sum += nums[end]
            if window_sum >= target:
                while window_sum >= target:
                    window_sum -= nums[start]
                    start += 1
                window_len = end - start + 2
                min_window_len = min(window_len, min_window_len)
        if min_window_len == float('inf'):
            min_window_len = 0
        return min_window_len
