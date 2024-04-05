"""
1456. Maximum Number of Vowels in a Substring of Given Length
(Medium complexity)

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}  # множество гласных букв
        cur = sum([1 if sym in vowels else 0 for sym in s[:k]])  # текущее значение счетчика гласных в окне k
        ans = cur  # ответ
        for i in range(k, len(s)):  # проходим по оставшимся буквам
            if s[i - k] in vowels:  # если убираемая из окна буква гласная - уменьшаем счетчик
                cur -= 1
            if s[i] in vowels:  # если добавляемая в окно буква гласная - увеличиваем счетчик, обновляем ответ
                cur += 1
                ans = max(ans, cur)
        # ответ
        return ans
