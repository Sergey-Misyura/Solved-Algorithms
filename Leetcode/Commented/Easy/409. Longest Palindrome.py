"""
409. Longest Palindrome
(Easy complexity)

Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
Palindrome
A palindrome is a string that reads the same forward and backward.

 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""


import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for v in collections.Counter(s).items():  # проходим по элементам в счетчике символов
            ans += v[1] // 2 * 2  # увеличиваем ответ на количество из v кратное 2
            if ans % 2 == 0 and v[1] % 2 == 1:  # для первого нечетного v - увеличиваем ответ на 1
                ans += 1
        # ответ
        return int(ans)