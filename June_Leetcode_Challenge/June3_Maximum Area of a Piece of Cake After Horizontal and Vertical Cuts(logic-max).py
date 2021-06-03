class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        '''
        Each pair of adjacent vertical slices leaves a slice of cake, affected by all horizontal cake.
        Conversely, every adjacent pair of adjacent horizontal cuts leaves a horizontal slice of cake.
        Makes sense to now just chose the overlap of the largest vertical slice and horizontal slice.
        Find the largest gap in vertical and horizontal arrays, muliply them together.
        Be sure to sort these arrays first.
        '''
        def find_largest_gap(in_array, dimension):
            '''
            Find the largest gap between adjacent cuts in the cake.
            Make a copy so you don't modify the mutable input
            '''
            # Edge cases for empty array or dimensionless
            if not in_array:
                return dimension
            if dimension == 0: return 0

            # Sort the array and add
            cur = 0
            max_gap = 0
            copy_array = in_array.copy()
            copy_array.sort()
            copy_array.append(dimension)

            # Iterate through cuts to find largest gap
            for i, cut in enumerate(copy_array):
                gap = cut - cur
                max_gap = max(max_gap, gap)
                cur = cut
            return max_gap

        hor_gap = find_largest_gap(horizontalCuts, h)
        vert_gap = find_largest_gap(verticalCuts, w)

        # need modulo per question requirements
        return (hor_gap * vert_gap) % 1000000007
            
