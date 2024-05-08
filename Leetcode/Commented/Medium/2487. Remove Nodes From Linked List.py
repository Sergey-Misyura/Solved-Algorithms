"""
2487. Remove Nodes From Linked List
(Medium complexity)

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_link_l(head):  # функция разварота списка
            cur = None
            while head:
                head.next, head, cur = cur, head.next, head
            return cur

        head = reverse_link_l(head)  # разворачиваем список
        cur, max_val = head, float('-inf')  # текущий указатель, текущее макс значение в пройденном списке
        while cur and cur.next:  # проходим по списку до последнего элемента
            max_val = max(max_val, cur.val)  # обновляем max_val
            next_node = cur.next  # новый указатель с следующего элемента
            while next_node and next_node.val < max_val:  # двигаем next_node пока в элементах val < max_val
                next_node = next_node.next
            cur.next = next_node  # перебрасываем next от cur на next_node
            cur = cur.next
        # ответ снова разворачиваем список
        return reverse_link_l(head)