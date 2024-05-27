"""
140. Word Break II
(Hard complexity)

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}  # кеш разбиваемых последоательностей

        def word_break(s):
            if s not in cache:  # если еще не разбивали
                res = []  # список разбивок для текущей s
                for cur_word in wordDict:  # проходим по словарю
                    if s[:len(cur_word)] == cur_word:  # если нашли в s cur_word
                        if len(s) == len(cur_word):  # если s является cur_word - добавляем в res
                            res.append(cur_word)
                        else:  # иначе рекурсивно вызываем word_break, для оставшейся части от s
                            for next_word in word_break(s[len(cur_word):]):
                                res.append(cur_word + ' ' + next_word)  # записываем разбивку в res
                cache[s] = res  # переносим для текущей s весь res в cache
            return cache[s]  # возвращаем список разбивок для s
        # ответ
        return word_break(s)