class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        one by one add elements all subsets to generate every combination
        '''
        out_lists = [[]]
        for num in nums:
            for elem in out_lists.copy():
                out_lists.append(elem + [num])
        return out_lists

            
