class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Instead of finding the fewest to erase directly, we can instead find the maximum number of intervals we can chosse without overlap. The cardinality of the origional set less the cardinality of this set will give the minimum number of intervals that need to be removed.
        O(nlogn) to sort + O(n) to greedily choose intervals => O(nlogn)
        '''
        def sort_interval_by_finish(intervals):
            '''Sort intervals by finish time'''
            intervals.sort(key = lambda x: x[1])
            return intervals

        def greedy_choose_earliest_finish(sorted_intervals):
            '''Greedily choose the earliest intervals based on finish time.
                This greedy strategy will choose intervals optimally.
            '''
            last_finish = float('-inf')
            new_intervals = []
            for interval in sorted_intervals:
                start, end = interval[0], interval[1]
                if start >= last_finish:
                    new_intervals.append(interval)
                    last_finish = end
            return new_intervals

        intervals = sort_interval_by_finish(intervals)
        new_intervals = greedy_choose_earliest_finish(intervals)
        return len(intervals) - len(new_intervals)
