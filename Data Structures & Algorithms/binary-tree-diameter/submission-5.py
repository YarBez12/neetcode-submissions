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
        self.diameterOfChildren(root)
        return self.maxDiameter

    def diameterOfChildren(self, root):
        if not root or not (root.left or root.right): 
            return 0
        curr = 0
        l = r = 0
        if root.left:
            l = self.diameterOfChildren(root.left)
            curr += l + 1
        if root.right:
            r = self.diameterOfChildren(root.right)
            curr += r + 1
        self.maxDiameter = max(self.maxDiameter, curr)
        return max(l, r) + 1
        