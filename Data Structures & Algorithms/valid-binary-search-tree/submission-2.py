# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ok, _, _ = self.check(root)
        return ok

    def check(self, node):
        if not node:
            return True, float("inf"), float("-inf")

        okLeft, leftMin, leftMax = self.check(node.left)
        okRight, rightMin, rightMax = self.check(node.right)
        if okLeft and okRight and node.val > leftMax and node.val < rightMin:
            return True, min(node.val, leftMin), max(rightMax, node.val) 
        return False, 0, 0
        