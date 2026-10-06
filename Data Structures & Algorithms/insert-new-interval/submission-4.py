class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        for interval in intervals:
            if newInterval and newInterval[0] > interval[1]:
                ans.append(interval)
            elif not newInterval or newInterval[1] < interval[0]:
                if newInterval:
                    ans.append(newInterval)
                    newInterval = None
                ans.append(interval)
            else:
                newInterval = min(interval[0], newInterval[0]), max(interval[1], newInterval[1])
        if newInterval:
            ans.append(newInterval)
        
        return ans
            

        