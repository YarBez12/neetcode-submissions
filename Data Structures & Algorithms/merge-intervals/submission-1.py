class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for interval in intervals:
            if ans and ans[-1][1] >= interval[0]:
                last = ans.pop()
                interval = [last[0], max(last[1], interval[1])]
            ans.append(interval)
        return ans
        