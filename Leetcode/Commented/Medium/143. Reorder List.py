"""
143. Reorder List
(Medium complexity)

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:  # если нет корня - ответ []
            return []

        # находим середину
        slow, fast = head, head  # медленный, быстрый указатели
        while fast.next and fast.next.next:  # пока можем передвигать fast
            slow = slow.next  # двигаем slow
            fast = fast.next.next  # двигаем fast

        # разворот хвоста списка
        prev, cur = None, slow.next  # предыдущий узел в развернутом списке, текущий узел в разворачиваемой части
        while cur:  # пока есть текущий узел
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        slow.next = None

        # соединения двух списков
        head1, head2 = head, prev  # указатель на начало исходного списка, указатель на начало развернутого
        while head2:
            next_node = head1.next
            head1.next = head2
            head1 = head2
            head2 = next_node