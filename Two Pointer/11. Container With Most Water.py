class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Area is (end-start) * min(height[start], height[end])
        lets try working from the outside in
        if the left wall is bigger than the right wall, then moving the left wall in is irrelevant because
            the height is capped by the height of the right wall and width will be guarenteed to be smaller.
        so, we can work from the outside in, and always move in the wall that is shorter
        compare the current volume to the max volume, and return max volume at the end.

        '''
        start, end = 0, len(height)-1
        max_volume = 0
        while end>start:
            volume = (end-start) * min(height[start], height[end])
            max_volume = max(max_volume, volume)
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        return max_volume

        
