class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        i = 0
        if newInterval[0] < intervals[0][0]:
            intervals.insert(0, newInterval)
        else:
            length = len(intervals) - 1
            for i in range(len(intervals)):
                if i < length and intervals[i][0] <= newInterval[0] <= intervals[i + 1][0]:
                    intervals.insert(i + 1, newInterval)
                    break
                if i == length:
                    intervals.insert(i + 1, newInterval)
        return self.merge(intervals)

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
