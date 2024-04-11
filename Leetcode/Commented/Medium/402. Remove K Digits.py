"""
402. Remove K Digits
(Medium complexity)

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # стек
        for sym in num:  # проходим по цифрам
            while stack and stack[-1] > sym and k > 0:  # если текущая цифра меньше цифры в стеке и есть k - убираем цифру из стека
                stack.pop()
                k -= 1
            stack.append(sym)  # ложим текущую цифру в стек
        while k > 0:  # если еще осталось k, убираем последние k цифр в стеке
            stack.pop()
            k -= 1
        # ответ
        if not stack:  # если стек пуст - ответ 0
            return '0'
        else:  # если есть цифры в стеке
            i = 0  # текущий индекс в стеке
            while i < len(stack) and stack[i] == '0':  # убираем начальные 0
                i += 1
            if i == len(stack):  # если все 0 в стеке - ответ 0
                return '0'
            else:  # иначе выводим число из стеке без первых 0
                return ''.join(stack[i:])