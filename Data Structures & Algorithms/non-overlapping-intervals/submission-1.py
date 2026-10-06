class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        num = 0
        end = float("-inf")
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
                continue
            num +=1
            end = min(end, interval[1])
        return num
        