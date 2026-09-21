# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, current):
            if not node:
                return 0, -1
            lCount, lMin = dfs(node.left, current)
            if lCount >= current:
                return current, lMin
            if lCount + 1 >= current:
                return current, node.val
            rCount, rMin = dfs(node.right, current - lCount-1)
            if rCount == current - lCount-1:
                return current, rMin
            return rCount + lCount + 1, -1
            
        _, ans = dfs(root, k)
        return ans
        