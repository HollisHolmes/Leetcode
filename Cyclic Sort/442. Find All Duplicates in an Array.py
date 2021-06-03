class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        Mostly based on the cycle sort, but in this case there are 2 main differences:
        1) there are only n possible values, so they will all fit into a slot in the array (shifted by 1)
        2) we need to keep track of duplicates

        We have found a duplicate if, the value at the current index cant be moved to slot current value -1,
            because that value is already there. Hence, add it to the set and move to next index.
        If it isnt laready a match, or isnt a duplicate, then swap like in a cyclic sort.
        '''
        n = len(nums)
        i = 0
        duplicates = set()
        while i < n:
            cur_val = nums[i]
            if i + 1 == cur_val:
                i += 1
                continue
            if cur_val == nums[cur_val - 1]:
                duplicates.add(nums[i])
                i += 1
                continue
            nums[i], nums[cur_val-1] = nums[cur_val-1], nums[i]

        return list(duplicates)
            
