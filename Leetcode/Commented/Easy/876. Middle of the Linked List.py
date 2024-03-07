"""
876. Middle of the Linked List
(Easy complexity)

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head  # медленный, быстрый указатели
        while fast and fast.next:  # пока есть текущий и следующий, двигаем указатели
            fast = fast.next.next
            slow = slow.next
        # возвращаем середину - узел указателя slow
        return slow