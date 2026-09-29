class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(curr, ind, ans):
            ans.append(curr.copy())
            if ind >= len(nums):
                return
            for i in range(ind, len(nums)):
                if i != ind and nums[i-1] == nums[i]:
                    continue
                curr.append(nums[i])
                backtrack(curr, i+1, ans)
                curr.pop()
        backtrack([], 0, ans)
        return ans
        