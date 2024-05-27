"""
1255. Maximum Score Words Formed by Letters
(Hard complexity)

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
"""


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = Counter(letters)  # счетчик количеств букв в letters

        def contains(container, contained):  # функция проверки содержания одного dict в другом
            return all(container[x] >= contained[x] for x in contained)

        def define_score(count):  # функция подсчета текущего score по dict
            return sum([score[ord(key) - 97] * value for key, value in count.items()])

        def calc(i, count):  # функция подсчета score для текущего слова
            if i >= len(words):  # если уже прошли все слова - возвращаем 0
                return 0
            cur_score = 0  # возвращаемый score
            cur_count = Counter(words[i])  # dict букв в слове
            if contains(count, cur_count):  # если мы можем включить слово в набор
                # обновляем cur_score как score текущего слова + рекурсивный вызов calc на следующее слова
                cur_score = define_score(cur_count) + calc(i + 1, count - cur_count)
            cur_score = max(cur_score, calc(i + 1, count))  # обновляем cur_score при невключении слова в набор и рекурсивного calc
            return cur_score

        all_score = []  # массив общего score при включении каждого слова
        for i in range(len(words)):  # проходим по словам
            all_score.append(calc(i, count))  # вызываем функцию подсчета общего score для текущего слова
        # ответ
        return max(all_score)
