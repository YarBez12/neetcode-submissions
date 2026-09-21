# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.preorderIndex = 0
        self.inorderMap = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.inorderMap[inorder[i]] = i
        return self.arrayToTree(preorder, 0, len(preorder)-1)
        

    def arrayToTree(self, preorder, left, right):
        if (left > right):
            return None
        rootValue = preorder[self.preorderIndex]
        self.preorderIndex += 1

        root = TreeNode(rootValue)
        root.left = self.arrayToTree(preorder, left,  self.inorderMap[rootValue]-1)
        root.right = self.arrayToTree(preorder,  self.inorderMap[rootValue]+1, right)

        return root