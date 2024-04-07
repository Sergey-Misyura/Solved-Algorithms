"""
678. Valid Parenthesis String
(Medium complexity)

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        count_min = count_max = 0  # минимальный диапазон, максимальный диапазон символов
        for sym in s:  # проходим по символам в s
            if sym == ')':  # при закрывающей скобке уменьшаем счетчик count_max
                count_max -= 1
            else:  # иначе увеличиваем счетчик count_max
                count_max += 1
            if sym == '(':  # при открывающей скобке увеличиваем счетчик count_min
                count_min += 1
            else:  # уменьшаем count_min
                count_min = max(count_min - 1, 0)
            if count_max < 0:  # если максимальный диапазон отрицательный - ответ False
                return False
        # ответ
        return count_min == 0