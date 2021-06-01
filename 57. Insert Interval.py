class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Go through each interval making constant numbe of comparisons  O(n) time
        If the interval is earlier than the new interval, add it to the new intervals
        If the interval is later than the new interval, add it to the new intervals
        If there is overlap, set the new start time for this inserted interval to the min of their starts
            and set the end to be the max of their ends
        before returning, add this one other interval that has the new start end end time
        '''
        if not intervals:
            return [newInterval]
        new_start, new_end = newInterval[0], newInterval[1]
        new_intervals = []
        for i, interval in enumerate(intervals):
            # earlier than new interval
            if interval[1] < new_start:
                new_intervals.append(interval)
            elif interval[0] > new_end:
                return new_intervals + [[new_start, new_end]] + intervals[i:]
            # intervals overlap
            else:
                new_start = min(new_start, interval[0])
                new_end = max(new_end, interval[1])

        new_intervals.append([new_start, new_end])
        return new_intervals
