# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = k
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        curr = head
        prev = None
        currHead = head
        prevHead = dummy
        while curr != None:
            if count == k:
                if curr != head:
                    prevHead = currHead
                    currHead = curr
                test = curr
                currCount = count
                while test != None and currCount > 0:
                    currCount -= 1
                    test = test.next
                if currCount:
                    prevHead.next = curr
                    break
            if count <= 1:
                temp = curr.next
                curr.next = prev
                prev = None
                prevHead.next = curr
                curr = temp
                count = k
            else:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1
        return dummy.next
        