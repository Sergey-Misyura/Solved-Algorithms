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
        revers = None  # обратный список
        slow = fast = head  # быстрый и медленный указатели
        while fast and fast.next:  # проходим до середины, разворачивая первую половину списка в reverse
            fast = fast.next.next
            revers, revers.next, slow = slow, revers, slow.next
        if fast:  # если список нечетной длины, еще шаг
            slow = slow.next
        while revers and revers.val == slow.val:  # проходим второй половине первого списка и reverse списку пока элементы одинаковы
            slow = slow.next
            revers = revers.next
        return not revers  # ответ