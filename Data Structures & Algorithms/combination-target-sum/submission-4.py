class Solution:
    # 1st approach
    # def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     nums.sort()
    #     ans = []
    #     def backtrack(curr, currSum, ind, ans):
    #         for i in range(ind, len(nums)):
    #             if currSum + nums[i] > target:
    #                 break
    #             curr.append(nums[i])
    #             currSum += nums[i]
    #             if currSum == target:
    #                 ans.append(curr.copy())
    #             backtrack(curr, currSum, i, ans)
    #             curr.pop()
    #             currSum -= nums[i]
        
    #     backtrack([], 0, 0, ans)
    #     return ans

    # 2nd approach
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(curr, ind, ans, target):
            if target == 0:
                ans.append(curr.copy())
            elif target < 0:
                return
            else:
                for i in range(ind, len(nums)):
                    curr.append(nums[i])
                    backtrack(curr, i, ans, target-nums[i])
                    curr.pop()
        
        backtrack([], 0, ans, target)
        return ans
        