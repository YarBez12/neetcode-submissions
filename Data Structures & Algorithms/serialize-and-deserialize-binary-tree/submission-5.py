# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        def dfs(node, arr):
            if not node:
                arr.append("null")
                return
            arr.append(str(node.val))
            dfs(node.left, arr)
            dfs(node.right, arr)
        dfs(root, data)
        return "#".join(data)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("#")
        def dfs(data, ind):
            if data[ind] == "null":
                return None, ind
            curr = TreeNode(data[ind])
            curr.left, ind = dfs(data, ind+1)
            curr.right, ind = dfs(data, ind+1)
            return curr, ind
        root, _ = dfs(data, 0)
        return root

