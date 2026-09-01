class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        res = 1
        for num in numSet:
            if (num-1) in numSet:
                continue
            curr = 1
            currNum = num
            while (currNum + 1) in numSet:
                currNum += 1
                curr += 1
            res = max(res, curr)
        
        return res

        