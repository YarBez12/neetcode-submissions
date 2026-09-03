# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        prev = None
        while curr1 and curr2:
            if curr1.val < curr2.val:
                # temp = curr1.next
                # if temp and temp.val < curr2.val:
                #     curr1 = temp
                # else:
                #     curr1.next = curr2
                #     curr1 = temp
                temp = curr1.next
                if prev:
                    prev.next = curr1
                else:
                    prev = curr1
                prev = curr1
                curr1 = temp
            else:
                # temp = curr2.next
                # if temp and temp.val < curr1.val:
                #     curr2 = temp
                # else:
                #     curr2.next = curr1
                #     curr2 = temp
                temp = curr2.next
                if prev:
                    prev.next = curr2
                else:
                    prev = curr2
                prev = curr2
                curr2 = temp
        prev.next = curr1 if curr1 else curr2
        return list1 if list1.val < list2.val else list2
        