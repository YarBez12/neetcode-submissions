class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        x = len(nums1)
        y = len(nums2)
        n = x + y
        l = 0
        r = x
        while l <= r:
            partX = (l + r) // 2
            partY = (n+1) // 2 - partX
            
            xLeft = nums1[partX-1] if partX else float("-inf")
            xRight = nums1[partX] if partX < x else float("inf")
            yLeft = nums2[partY-1] if partY else float("-inf")
            yRight = nums2[partY] if partY < y else float("inf")
            if xLeft <= yRight and yLeft <= xRight:
                if (x + y) % 2:
                    return max(xLeft, yLeft)
                else:
                    return (max(xLeft, yLeft) + min(xRight, yRight)) / 2
            elif xLeft > yRight:
                r = partX - 1
            else:
                l = partX + 1
        
        return 0


        