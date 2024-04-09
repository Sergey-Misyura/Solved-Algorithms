"""
791. Custom Sort String
(Medium complexity)

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)  # счетчик букв целевой строке
        answer = []  # ответ
        for sym in order:  # проходим по order, добавляем буквы из count по их количеству
            rep = count.pop(sym, 0)
            answer.append(sym * rep)
        answer.extend([key * value for key, value in count.items()])  # добавляем оставшиеся буквы из count
        # ответ
        return ''.join(answer)