class Solution:
    # 1st approach 

    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     if not intervals:
    #         return [newInterval]
    #     ans = []
    #     for interval in intervals:
    #         if newInterval and newInterval[0] > interval[1]:
    #             ans.append(interval)
    #         elif not newInterval or newInterval[1] < interval[0]:
    #             if newInterval:
    #                 ans.append(newInterval)
    #                 newInterval = None
    #             ans.append(interval)
    #         else:
    #             newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
    #     if newInterval:
    #         ans.append(newInterval)
        
    #     return ans
    
    # 2nd approach
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)
        while i < n and newInterval[0] > intervals[i][1]:
            ans.append(intervals[i])
            i += 1
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        ans.append(newInterval)
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans
            

        