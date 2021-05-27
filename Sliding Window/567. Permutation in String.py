class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Count instances of each char in word 1, storing in a dictionary
        Move a sliding window of length len(s1) through s2, counting instances of each char in the window
        If count of each char in the sliding window is the same as count for s1, return True!
        If you reach the end without a short-circuit, return False
        '''
        start = 0
        len_s1 = len(s1)
        # Count chars in s1
        s1_count = {}
        for letter in s1:
            if letter not in s1_count:
                s1_count[letter] = 0
            s1_count[letter] += 1

        # Count chars in each sliding window of length len(s1) in O(1) each, O(n) total
        s2_window_count = {}
        for end in range(len(s2)):
            # Add right char
            right_char = s2[end]
            if right_char not in s2_window_count:
                s2_window_count[right_char] = 0
            s2_window_count[right_char] += 1
            # If we are at a full lenght window
            if end >= len_s1 - 1:
                # Check if we have a match, and return true
                if s2_window_count == s1_count:
                    return True
                # Remove the left char of the window that is falling out of range
                left_char = s2[end - len_s1 + 1]
                # Delete it if its count is one, otherwise decrement by 1
                if s2_window_count[left_char] == 1:
                    del s2_window_count[left_char]
                else:
                    s2_window_count[left_char] -= 1
                start += 1
        # If we dont find a match, return False
        return False

            
