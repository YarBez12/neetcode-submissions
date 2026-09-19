# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.count(root, root.val)
        return self.res
    

    def count(self, node, maximum):
        if not node:
            return
        if node.val >= maximum:
            self.res += 1
            maximum = node.val
        self.count(node.left, maximum)
        self.count(node.right, maximum)
        