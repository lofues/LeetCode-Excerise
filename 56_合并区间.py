class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                self.merge_interval(intervals, i)
            else:
                i += 1
        return intervals

    def merge_interval(self, intervals, i):
        last_item = max(intervals[i][1], intervals[i + 1][1])
        intervals.pop(i + 1)
        intervals[i][1] = last_item