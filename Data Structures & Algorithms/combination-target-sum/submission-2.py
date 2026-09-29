class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(curr, currSum, ind, ans):
            # curr.append(nums[ind])
            # currSum += nums[ind]
            for i in range(ind, len(nums)):
                curr.append(nums[i])
                currSum += nums[i]
                if currSum == target:
                    ans.append(curr.copy())
                    curr.pop()
                    currSum -= nums[i]
                    break
                if currSum > target:
                    curr.pop()
                    currSum -= nums[i]
                    break
                backtrack(curr, currSum, i, ans)
                curr.pop()
                currSum -= nums[i]
        
        backtrack([], 0, 0, ans)
        return ans
        