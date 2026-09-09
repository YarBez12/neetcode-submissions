# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, ok = self.getHeight(root)
        return ok

    def getHeight(self, root):
        if not root:
            return 0, True
        left, isLeftOK = self.getHeight(root.left)
        right, isRightOK = self.getHeight(root.right)
        if isLeftOK and isRightOK:
            return max(left, right) + 1, abs(left-right) <= 1
        else:
            return max(left, right) + 1, False
        