"""
648. Replace Words
(Medium complexity)

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.
"""



class Trie:
    def __init__(self):
        self.root = {}  # корневой словарь

    def insert(self, word):
        node = self.root
        for char in word:  # проходим по символу в слове
            if char not in node:  # если еще не было - добавляем как новый словарь
                node[char] = {}
            node = node[char]  # переходим к вложенному словарю
        node['#'] = True  # помечаем конец слова

    def search(self, word):
        node = self.root
        ans = ''  # ответ
        for char in word:  # спускаемся по буквам искомого слова по дереву root
            if char in node:
                ans += char  # изменяем ответ
                node = node[char]
                if '#' in node:  # когда нашли первый самый короткий "корень" завершаем цикл
                    break
            else:  # если нет буквы в поддереве - завершаем цикл
                break
        # возвращаем замененное слово если нашли, иначе искомое
        return ans if "#" in node else word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()  # создаем преф дерево
        for word in dictionary:  # проходим по словам и добавляем в дерево
            trie.insert(word)
        # возвращаем ответ - предложение с замененными словами из дерева
        return ' '.join(map(trie.search, sentence.split()))