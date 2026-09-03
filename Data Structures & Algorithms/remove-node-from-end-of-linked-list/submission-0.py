# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        h1 = head
        h2 = head
        for i in range(n):
            h2 = h2.next
        while h2:
            prev = h1
            h1 = h1.next
            h2 = h2.next
        if not prev:
            head = h1.next
        else:
            prev.next = h1.next
        return head
        