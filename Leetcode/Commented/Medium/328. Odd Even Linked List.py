"""
328. Odd Even Linked List
(Medium complexity)

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:  # частный случай
            return head

        odd = even = head  # указатели четного и нечетного узлов
        even = even.next  # переход по четному
        even_head = even  # указатель на начало четного
        while even and even.next:  # пока есть четный и узел за ним
            odd.next, even.next = odd.next.next, even.next.next  # соединяем четный и нечетные узлы через 1
            odd, even = odd.next, even.next  # переходим к следующим узлам по соединениям
        # добавляем к списку нечетных - список четных
        odd.next = even_head
        # ответ
        return head