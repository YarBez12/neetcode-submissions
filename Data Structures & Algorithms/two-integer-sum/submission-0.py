class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in numToIndex:
                return [numToIndex[curr], i]
            numToIndex[nums[i]] = i

        