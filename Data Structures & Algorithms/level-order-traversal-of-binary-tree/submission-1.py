# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrderMaker(root, [], 0)
    

    def levelOrderMaker(self, root, arr, level):
        if root == None:
            return arr
        if len(arr) <= level:
            arr.append([])
        arr[level].append(root.val)
        arr = self.levelOrderMaker(root.left, arr, level+1)
        arr = self.levelOrderMaker(root.right, arr, level+1)

        return arr

        