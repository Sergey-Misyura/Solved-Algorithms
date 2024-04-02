"""
1768. Merge Strings Alternately
(Easy complexity)

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)

        ans = [0] * (2 * min(n, m))  # массив ответа
        cur_n, cur_m = 0, 0  # указатели в word1 и word2
        cur_ans = 0  # указатель в ans
        while cur_n < n and cur_m < m:  # пока не вышли за один из массивов
            ans[cur_ans] = word1[cur_n]  # добавляем в ответ букву из word1
            cur_ans += 1
            cur_n += 1
            ans[cur_ans] = word2[cur_m]  # добавляем в ответ букву из word2
            cur_ans += 1
            cur_m += 1

        ans = ''.join(ans)  # составляем строку из ans
        # ответ
        if n == m:  # выводим ответ если добавили все символы
            return ans
        elif n > m:  # иначе если длина word1 больше word2, добавляем к ответу хвост из word1
            return ans + word1[cur_n:]
        else:  # иначе добавляем к ответу хвост из word2
            return ans + word2[cur_m:]