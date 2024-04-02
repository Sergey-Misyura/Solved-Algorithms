"""
1071. Greatest Common Divisor of Strings
(Easy complexity)

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2."""

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:  # если при переставление строки не одинаковы, значит их нельзя разбить общей подстрокой - ответ False
            return ""
        # иначе, ответ есть,
        # в ответе возвращаем обрезанную по наибольшему общему делителю первую строку
        return str1[:gcd(len(str1), len(str2))]