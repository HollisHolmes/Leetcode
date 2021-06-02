class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Can't simply us a greedy approach, need to use dynamic programming.
        State is the letters used in each word, depends on one less letter used in either word.
        '''
        # Length of all input strings
        m = len(s1)
        n = len(s2)
        l = len(s3)

        # Sum of s1 and s2 lengths must equal length of s3 for this to be possible
        if m+n != l: return False

        # Create DP table of 0's
        DP = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                # Empty string is  always a match
                if i == 0 and j == 0: DP[i][j] = 1
                # First row, be sure to only check left as there is no row above to check
                elif i == 0:
                    DP[i][j] = DP[i][j-1] and s3[j-1] == s2[j-1]
                # First col, be sure to only check up as there is no col left to check
                elif j == 0:
                    DP[i][j] = DP[i-1][j] and s3[i-1] == s1[i-1]
                # Check both dependents for a match (left using letter from s2 or up using letter from 1)
                # Either one working yields a true
                else:
                    DP[i][j] = DP[i][j-1] and s3[j+i-1] == s2[j-1] or  DP[i-1][j] and s3[i+j-1] == s1[i-1]

        return DP[-1][-1]
