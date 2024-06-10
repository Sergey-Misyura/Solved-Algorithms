"""
1002. Find Common Characters
(Easy complexity)

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        total_counts = Counter(words[0])  # счетчик букв в первом слове
        for word in words[1:]:  # проходим по остальным словам
            total_counts = total_counts & Counter(word)  # находим пересечение текущих общих символов с каждым последующим словом
        # разворачиваем ответ
        return list(total_counts.elements())