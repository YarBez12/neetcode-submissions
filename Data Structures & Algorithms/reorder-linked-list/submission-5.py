# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        i1 = head
        i2 = prev
        while i1 and i2:
            temp1 = i1.next
            temp2 = i2.next
            i1.next = i2
            i2.next = temp1 if temp1 else temp2
            i1 = temp1
            i2 = temp2
        
        