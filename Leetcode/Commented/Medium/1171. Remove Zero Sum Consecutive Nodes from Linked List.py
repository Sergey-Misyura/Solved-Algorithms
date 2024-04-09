"""
1171. Remove Zero Sum Consecutive Nodes from Linked List
(Medium complexity)

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = temp = ListNode(0)  # указатель ответа, текущий указатель
        temp.next = head
        pref_sum = 0  # преф сумма
        sums_dict = OrderedDict()  # словарь преф сумм
        while cur:  # проходим по списку
            pref_sum += cur.val  # увеличиваем преф сумму
            node = sums_dict.get(pref_sum, cur)  # получаем преф сумму из sums_dict
            while pref_sum in sums_dict:  # откатываем значения в словаре
                sums_dict.popitem()
            sums_dict[pref_sum] = node  # сохранеям узел
            node.next = cur = cur.next  # удаляем подсписок с суммой 0
        # ответ
        return temp.next