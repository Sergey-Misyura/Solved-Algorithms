"""
1915. Number of Wonderful Substrings
(Medium complexity)

A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt, ans, mask = [1] + [0] * 1023, 0, 0  # количество замечательных строк для битовых масок, ответ, битовая маска
        for sym in word:  # для каждого символа в word
            mask ^= 1 << (ord(sym) - ord('a'))  # переключаем бит в битовой маске, соответствующий символу
            ans += cnt[mask]  # увеличиваем ответ на число в cnt[mask]
            for n in range(10):  # добавляем число подстрок в которых перестановка 1 бита дает замечательную подстроку
                ans += cnt[mask ^ 1 << n]  # увеличиваем на cnt после переключения 1 бита
            cnt[mask] += 1  # увеличиваем количество по текущей битмаске
        # ответ
        return ans