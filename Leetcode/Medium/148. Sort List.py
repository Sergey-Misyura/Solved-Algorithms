"""
148. Sort List
(Medium complexity)

Given the head of a linked list, return the list after sorting it in ascending order.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(start)
        return self.merge(left, right)

    def merge(self, l, r):
        dummy = tail = ListNode(None)
        while l and r:
            if l.val < r.val:
                tail.next, tail, l = l, l, l.next
            else:
                tail.next, tail, r = r, r, r.next

        tail.next = l or r
        return dummy.next