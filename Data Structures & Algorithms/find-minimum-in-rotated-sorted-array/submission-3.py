class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        l = 1
        r = len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m-1] and (m == len(nums) -1 or nums[m] < nums[m+1]):
                return nums[m]
            elif nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1
        
        return -10000


        