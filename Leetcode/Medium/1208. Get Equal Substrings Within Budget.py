"""
1208. Get Equal Substrings Within Budget
(Medium complexity)

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        lf = 0  # левый указатель
        for rg in range(len(s)):  # проходим правым указателем по s и t
            maxCost -= abs(ord(s[rg]) - ord(t[rg]))  # уменьшаем maxCost (кумулятивное значение разниц на [lf, rg]) на разницу символов
            if maxCost < 0:  # если вышли за границы допустимой стоимости
                maxCost += abs(ord(s[lf]) - ord(t[lf]))  # двигаем левую границу, увеличивая maxCost
                lf += 1
        # ответ
        return rg - lf + 1
