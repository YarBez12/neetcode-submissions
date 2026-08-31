class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = {0: 1}
        after = {(len(nums)-1): 1}
        mult = 1
        for i in range(1, len(nums)):
            mult *= nums[i-1]
            before[i] = mult
        mult = 1
        for j in range(len(nums)-2, -1, -1):
            mult *= nums[j+1]
            after[j] = mult
        
        ans = []
        for k in range(len(nums)):
            ans.append(before[k] * after[k])
        
        return ans
        