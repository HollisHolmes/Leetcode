class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        Lists are both disjoint and in sorted order, which prevents us from needing to do an initial sort.
        We can now simply move through each list in sync, iterating past which ever interval has an earlier finish              time. If there is an overlap record it before moving on
        '''
        i, j = 0, 0
        start, end = 0, 1
        intersect = []

        # Loop through both lists until you are all the way through either of the lists
        # At that point there are no more intersections
        while i < len(firstList) and j < len(secondList):
            # Check if there is an overlap (one start time falls into the range of the other)
            overlap = firstList[i][start] >= secondList[j][start] and firstList[i][start] <= secondList[j][end] \
                    or secondList[j][start] >= firstList[i][start] and secondList[j][start] <= firstList[i][end]
            # If overlap, calculate it and add it to the intersects list
            if overlap:
                inter_start = max(firstList[i][start], secondList[j][start])
                inter_end = min(firstList[i][end], secondList[j][end])
                intersect.append([inter_start, inter_end])
           # Move pointer on whichever list has the current interval that ends first
            if firstList[i][end] < secondList[j][end]:
                i += 1
            else:
                j += 1

        return intersect
                
