class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_char_map = {} #track latest occurance of each char, if a second appears need to move window at least to here
        start = 0  #index for start of moving window
        longest = 0 #track longest window seen
        #loop through all possible ending points for the window, adjusting start as needed
        for end in range(len(s)):
            right_char = s[end]
            # if this is char first occurance, we just extend the window by one
            if right_char not in last_char_map:
                last_char_map[right_char] = end
            # if this char is already in the window, can't just add it need to adjust the starting point
            else:
                #update the start of the window, however, if the start has already been moved past the
                # the previous instance of the char we dont want to move it back, this would make the window invalid
                # so we set the start to be the max of where the start is rn, and where the last occurance of the char is
                start = max(last_char_map[right_char]+1, start)
                last_char_map[right_char] = end
            # calculate window length and check if it is longer than previous longest
            window_len = end-start+1
            longest = max(longest, window_len)

        return longest
