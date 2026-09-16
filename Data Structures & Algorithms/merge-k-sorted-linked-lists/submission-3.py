# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #1st approach
        # dummy = ListNode(0)
        # prev = dummy
        # while True:
        #     m = 100000
        #     ind = -1
        #     for l in range(len(lists)):
        #         if lists[l] and lists[l].val < m:
        #             m = lists[l].val
        #             ind = l
        #     if ind == -1:
        #         break
        #     prev.next = lists[ind]
        #     lists[ind] = lists[ind].next
        #     prev = prev.next
        # return dummy.next

        #2nd approach

        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        if len(lists) == 2:
            curr1 = lists[0]
            curr2 = lists[1]
            if curr1 == None:
                return curr2
            if curr2 == None:
                return curr1
            dummy = ListNode(0)
            prev = dummy
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    prev.next = curr1
                    curr1 = curr1.next
                else:
                    prev.next = curr2
                    curr2 = curr2.next
                prev = prev.next
            prev.next = curr1 if curr1 else curr2
            return dummy.next
        else:
            m = len(lists) // 2
            l1 = self.mergeKLists(lists[:m])
            l2 = self.mergeKLists(lists[m:])
            return self.mergeKLists([l1, l2])