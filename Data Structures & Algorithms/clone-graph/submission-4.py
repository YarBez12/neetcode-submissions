"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = {node.val:Node(node.val)}
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()
            currCopy = nodes[curr.val]
            neighborsCopy = []
            for neigh in curr.neighbors:
                if neigh.val in nodes:
                    neighCopy = nodes[neigh.val]
                else:
                    neighCopy = Node(neigh.val)
                    nodes[neigh.val] = neighCopy
                    q.append(neigh)
                neighborsCopy.append(neighCopy)
            currCopy.neighbors = neighborsCopy
        return nodes[node.val]

        