"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        d = {}
        p = head
        while p != None:
            d[p] = Node(p.val)
            p = p.next
        newHead = d[head]
        p1 = newHead
        p2 = head
        while p2 != None:
            if p2.next:
                p1.next = d[p2.next]
            if p2.random:
                p1.random = d[p2.random]
            p1 = p1.next
            p2 = p2.next

        return newHead