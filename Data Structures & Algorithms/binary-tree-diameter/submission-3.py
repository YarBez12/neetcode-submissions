# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxDiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, ans = self.diameterOfChildren(root)
        return ans

    def diameterOfChildren(self, root):
        if not root or not (root.left or root.right): 
            return 0, 0
        curr = 0
        m = 0
        lMax = rMax = 0
        l = r = 0
        if root.left:
            l, lMax = self.diameterOfChildren(root.left)
            curr += l + 1
            m = max(m, lMax)
        if root.right:
            r, rMax = self.diameterOfChildren(root.right)
            curr += r + 1
            m = max(m, rMax)
        m = max(m, curr)
        return max(l, r) + 1, m
        