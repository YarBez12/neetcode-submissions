class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(curr, ind, ans):
            ans.append(curr.copy())
            if ind >= len(nums):
                return
            for i in range(ind, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1, ans)
                curr.pop()
        backtrack([], 0, ans)
        return ans
        