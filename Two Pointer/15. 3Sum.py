class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort the input arrat [O(nlogn)]
        now for each element except the last 2, loop through, and then run 2sum sorted on the rest of the array
        if there is a match append the resulting triplet
        skip duplicates
        '''
        def sorted_2sum(sorted_input, target):
            # 2 sum on a sorted array with 2 pointers
            indices = []
            start, end = 0, len(sorted_input)-1
            # unitl pointers meet
            while start < end:
                cur_sum = sorted_input[start] + sorted_input[end]
                # if match, add indices to list, skip over duplicates for beginning and end, then increment them 1 more time
                if cur_sum == target:
                    indices.append([start, end])
                    while start < end and sorted_input[start] == sorted_input[start+1]:
                        start += 1
                    while start < end and sorted_input[end] == sorted_input[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif cur_sum < target:
                    while start < end  and  sorted_input[start] == sorted_input[start+1]:
                        start += 1
                    start += 1
                elif cur_sum > target:
                    while start < end and sorted_input[end] == sorted_input[end-1]:
                        end -= 1
                    end -= 1
            # print('target: {} , ')
            return indices


        nums.sort()
        triplets = []
        for i, first_num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            twosum_target = -1*first_num
            twosum_pairs = sorted_2sum(nums[i+1:], twosum_target)
            triple = [[first_num, nums[pair[0]+i+1], nums[pair[1]+i+1]] for pair in twosum_pairs]
            triplets.extend(triple)
        return triplets
            
