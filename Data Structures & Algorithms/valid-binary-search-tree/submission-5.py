# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #1st approach
    #     ok, _, _ = self.check(root)
    #     return ok

    # def check(self, node):
    #     if not node:
    #         return True, float("inf"), float("-inf")

    #     okLeft, leftMin, leftMax = self.check(node.left)
    #     okRight, rightMin, rightMax = self.check(node.right)
    #     if okLeft and okRight and node.val > leftMax and node.val < rightMin:
    #         return True, min(node.val, leftMin), max(rightMax, node.val) 
    #     return False, 0, 0

        # 2nd approach
        prev = None

        def check(node):
            nonlocal prev
            if not node:
                return True
            if not check(node.left):
                return False
            if prev != None and node.val <= prev:
                return False
            prev = node.val
            return check(node.right)


        return check(root)
        