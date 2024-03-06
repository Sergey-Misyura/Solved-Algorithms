"""
141. Linked List Cycle
(Easy complexity)

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # медленный указатель
        fast = head  # быстрый указатель
        cycle = False  # флаг цикла
        # пока быстрый указатель может двигаться и не установлен флаг цикла
        while fast and fast.next and not cycle:
            slow = slow.next  # двигаем указатель
            fast = fast.next.next  # двигаем указатель
            cycle = slow == fast  # если указатели догнали друг друга - флаг True
        # вохвращаем флаг цикла
        return cycle