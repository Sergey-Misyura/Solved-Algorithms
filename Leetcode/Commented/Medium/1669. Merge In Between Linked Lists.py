"""
1669. Merge In Between Linked Lists
(Medium complexity)

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur1_node = list1  # ставим указатель текущего узла в первый узел первого дерева
        for i in range(a - 1):  # проходим к узлу перед удаляемым фрагментом
            cur1_node = cur1_node.next

        cur1_tail = cur1_node.next  # указатель хвостовой части первого списка
        for i in range(b - a + 1):  # проходим до первого элемента оставляемого хвоста
            cur1_tail = cur1_tail.next

        cur1_node.next = list2  # присоединеям второй список к части первого
        while cur1_node.next:  # проходим по соединенным элементам
            cur1_node = cur1_node.next

        cur1_node.next = cur1_tail  # к полученному списку добавляем хвост от первого списка
        # возвращаем итоговый список через указатель на первый список
        return list1