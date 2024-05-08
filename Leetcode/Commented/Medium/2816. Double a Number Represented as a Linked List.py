"""
2816. Double a Number Represented as a Linked List
(Medium complexity)

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_link_l(head):  # функция разворота списка
            cur = None
            while head:
                head.next, head, cur = cur, head.next, head
            return cur

        head = reverse_link_l(head)  # разворачиваем список
        cur, rem = head, 0  # текущий элемент, остаток большего разряда

        while cur.next:  # проходим по развернутому списку, до последнего элемента
            rem, cur.val = divmod(cur.val * 2 + rem, 10)  # считаем остаток и текущее значение в узле
            cur = cur.next
        rem, cur.val = divmod(cur.val * 2 + rem, 10)  # считаем остаток и текущее значение в узле для последнего элемента

        if rem > 0:  # если есть остаток более высокого порядка - добавляем с ним элемент
            cur.next = ListNode(rem)
        # ответ - снова разворачиваем получившийся список
        return reverse_link_l(head)