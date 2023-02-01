"""
2.Add Two Numbers
(Medium complexity)

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        cursor = result
        tens = 0

        while (l1 or l2 or tens):
            num_1 = l1.val if l1 else 0
            num_2 = l2.val if l2 else 0

            sum_nums = num_1 + num_2 + tens

            tens, num  = divmod(sum_nums, 10)

            cursor.next = ListNode(num)
            cursor=cursor.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next