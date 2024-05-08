"""
165. Compare Version Numbers
(Medium complexity)

Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int, version1.split('.')))  # переводим в список version1
        ver2 = list(map(int, version2.split('.')))  # переводим в список version2
        n = min(len(ver1), len(ver2))  # находим мин длину версий
        for i in range(n):  # проходим по n
            if ver1[i] > ver2[i]: # возвращаем 1 если ver1 больше ver2
                return 1
            elif ver1[i] < ver2[i]: # возвращаем -1 если ver2 больше ver1
                return -1
        if len(ver1) > n:  # если длина ver1 больше и они по n были одинаковы - проверяем на отличие от 0 оставшейся части списка ver1
            if any(ver1[n:]) > 0:
                return 1
        elif len(ver2) > n: # иначе, если длина ver2 больше и они по n были одинаковы - проверяем на отличие от 0 оставшейся части списка ver2
            if any(ver2[n:]) > 0:
                return -1
        # если все проверки пройдены - версии одинаковы, ответ 0
        return 0