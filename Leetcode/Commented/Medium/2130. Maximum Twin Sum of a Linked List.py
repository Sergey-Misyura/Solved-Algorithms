"""
2130. Maximum Twin Sum of a Linked List
(Medium complexity)

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next  # быстрый, медленный указатели
        rev = None  # указатель первого элемента развернутой первой части списка
        while fast.next:  # пока не дошли до конца списка
            fast = fast.next.next  # проходим быстрым указателем
            slow.next, slow, rev = rev, slow.next, slow  # разворачиваем первую часть списка, и двигаем указатель slow
        slow.next, slow, rev = rev, slow.next, slow  # еще 1 шаг, для перехода во вторую часть списка

        max_sum = 0  # макс сумма
        while slow:  # пока есть текущий элемент в slow - проходим по slow и rev спискам
            max_sum = max(max_sum, rev.val + slow.val)  # обновляем максимум суммы узлов
            rev =rev.next
            slow = slow.next
        # ответ
        return max_sum