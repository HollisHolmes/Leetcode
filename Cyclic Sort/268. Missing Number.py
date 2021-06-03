class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Here we have n+1 options ot be assigned into n slots in the array.
        We will iterate through the array, moving each item we come across into its correct slot.
        The only exception is if we come across the number n, in this case we will leave it in place for now,
            and catch it in out final pass when we are looking for the one number that we are missing.

        '''
        def cycle_sort_input_list(nums,n):
            i = 0
            while i < n:
                j = nums[i]
                if j == i or j == n:
                    i += 1
                    continue
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            return nums

        def check_missing(nums, n):
            for i, num in enumerate(nums):
                if i != num:
                    return i
            return n

        n = len(nums)
        nums = cycle_sort_input_list(nums, n)
        return check_missing(nums, n)
