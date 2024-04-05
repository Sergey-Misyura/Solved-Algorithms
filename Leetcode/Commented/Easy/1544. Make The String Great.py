"""
1544. Make The String Great
(Easy complexity)

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.
"""

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # стек
        for sym in s:  # проходим по s
            sym_ord = ord(sym)  # код символа
            if not stack or (stack and abs(stack[-1] - sym_ord) != 32):  # если стек пуст, или последний символ не текущий в другом регистре
                stack.append(sym_ord)  # добавляем код символа в стек
            else:  # иначе достаем код из стека
                stack.pop()
        # ответ - строка из стека
        return ''.join(map(chr,stack))
