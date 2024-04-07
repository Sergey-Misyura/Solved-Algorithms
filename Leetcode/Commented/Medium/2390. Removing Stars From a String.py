"""
2390. Removing Stars From a String
(Medium complexity)

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []  # стек
        for sym in s:  # проходим по символам в s
            if sym != '*':  # если не * - добавляем в стек
                stack.append(sym)
            else:  # иначе убираем последний символ из стека
                stack.pop()
        # ответ
        return ''.join(stack)