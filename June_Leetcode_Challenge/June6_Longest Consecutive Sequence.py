class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Here we leverage the O(1) lookup time for items in a set.
        First build a set out of the input numbers.
        Then keep checking if the numbers above it or below it are also in the set
            if they are, add 1 to sequence length and remove it from the set so we dont repeat computation
        Once you reached the end of the sequence, check if this sequence is longer or shorter than the previous             longest
        '''
        # Initialize has of list values
        num_set = set(nums)
        max_seq_len = 0
        for num in nums:
            # if we haven't already seen this number (and removed it from the set)
            if num in num_set:
                j, seq_len = 1, 1
                # keep checking if we can extend the high end of the sequence
                while num + j in num_set:
                    num_set.remove(num+j)
                    seq_len += 1
                    j += 1

                j = 1
                # keep changing the low end fo the sequence
                while num - j in num_set:
                    num_set.remove(num-j)
                    seq_len += 1
                    j += 1

            max_seq_len = max(max_seq_len, seq_len)
        return max_seq_len
                    
