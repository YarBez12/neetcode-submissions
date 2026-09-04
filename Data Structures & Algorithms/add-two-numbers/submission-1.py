# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        carry = 0
        dummy = ListNode(0, None)
        curr = dummy
        while h1 or h2 or carry:
            v1 = h1.val if h1 else 0
            v2 = h2.val if h2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            curr.next = ListNode(val % 10)
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
            curr = curr.next
        return dummy.next