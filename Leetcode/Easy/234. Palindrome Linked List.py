"""
234. Palindrome Linked List
(Easy complexity)

Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        revers = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            revers, revers.next, slow = slow, revers, slow.next
        if fast:
            slow = slow.next
        while revers and revers.val == slow.val:
            slow = slow.next
            revers = revers.next
        return not revers