class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans
    

    def backtrack(self, nums, curr, ans):
        if len(curr) == len(nums):
            ans.append(curr.copy())
            return

        for i in range(len(nums)):
            if nums[i] in curr:
                continue
            curr.append(nums[i])
            self.backtrack(nums, curr, ans)
            curr.pop()

        