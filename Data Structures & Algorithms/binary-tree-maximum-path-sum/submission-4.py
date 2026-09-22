# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxPath = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMax(root)
        return self.maxPath
    
    #1st approach
    # def findMax(self, root):
    #     if not root:
    #         return 0
    #     leftSum = self.findMax(root.left)
    #     rightSum = self.findMax(root.right)
    #     curr = max(root.val, root.val + leftSum, root.val + rightSum, root.val + leftSum + rightSum)
    #     self.maxPath = max(self.maxPath, curr)
    #     return max(root.val, root.val + leftSum, root.val + rightSum)

    # 2nd approach
    def findMax(self, root):
        if not root:
            return 0
        leftSum = max(0, self.findMax(root.left))
        rightSum = max(0, self.findMax(root.right))
        curr = root.val + leftSum + rightSum
        self.maxPath = max(self.maxPath, curr)
        return max(leftSum, rightSum) + root.val
        