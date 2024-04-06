"""
1249. Minimum Remove to Make Valid Parentheses
(Medium complexity)

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)  # переводим строку в список
        stack = []  # создаем стек
        for i in range(len(s)):  # проходим по s
            if s[i] == '(':  # если встретили открывающую скобку - добавляем в стек
                stack.append((s[i], i))
            elif s[i] == ')':  # если встретили закрывающую скобку
                if not stack or stack[-1][0] == ')':  # и можем закрыть предыдущую - закрываем
                    stack.append((s[i], i))
                else:  # иначе добавляем в стек
                    stack.pop()
        # проходим по символам в стеке, заменяем в s на ''
        for _, i in stack:
            s[i] = ''
        # ответ
        return ''.join(s)

