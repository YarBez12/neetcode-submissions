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
    
    def findMax(self, root):
        if not root:
            return float("-inf")
        leftSum = self.findMax(root.left)
        rightSum = self.findMax(root.right)
        curr = max(root.val, root.val + leftSum, root.val + rightSum, root.val + leftSum + rightSum)
        self.maxPath = max(self.maxPath, curr)
        return max(root.val, root.val + leftSum, root.val + rightSum)
        