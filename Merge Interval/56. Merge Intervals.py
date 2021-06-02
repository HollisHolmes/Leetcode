class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        sort by start time, then keep track of the start/end of internval rnge as you iterate through.
        If the current interval iterated interval overlaps the current range, extend the end to max(cur_end and end[i])         and move to next element,
        otherwise add the current interval and set the current one to be the the new range
        '''
        intervals.sort(key= lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        merged = []
        for i in range(1, len(intervals)):
            check_start = intervals[i][0]
            check_end = intervals[i][1]
            if end >= check_start:
                end = max(end, check_end)
                continue
            merged.append([start, end])
            start, end = check_start, check_end

        merged.append([start, end])

        return merged

            
