class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Use hash map to store the values we have already seen, and map them to their respective index

        '''
        complement_sum = {}
        for i, num in enumerate(nums):
            if num in complement_sum:
                return [i, complement_sum[num]]
            complement_sum[target - num] = i
