"""
345. Reverse Vowels of a String
(Easy complexity)

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)  # переходим от строки к списку s
        n = len(s)  # длина s
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E' , 'I', 'O', 'U'])  # множество гласных
        lf, rg = 0, n - 1  # два указателя
        while lf < rg:  #  пока указатели не сошлись
            while lf < n and s[lf] not in vowels:  # двигаем левую границу до гласной
                lf += 1
            while rg > -1 and s[rg] not in vowels:  # двигаем правую границу до гласной
                rg -= 1
            if lf < rg and lf < n and rg > -1:  # если не вышли за границы и не сошлись - обмениевам гласные
                s[lf], s[rg] = s[rg], s[lf]
                lf += 1; rg -= 1
        # ответ
        return ''.join(s)