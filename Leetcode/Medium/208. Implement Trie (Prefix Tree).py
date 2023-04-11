"""
208. Implement Trie (Prefix Tree)
(Medium complexity)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""


class Trie:

    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = False

    def insert(self, word: str) -> None:
        current = self
        for sym in word:
            current = current.children[sym]
        current.word = True

    def search(self, word: str) -> bool:
        current = self
        for sym in word:
            if sym not in current.children:
                return False
            current = current.children[sym]
        return current.word

    def startsWith(self, prefix: str) -> bool:
        current = self
        for sym in prefix:
            if sym not in current.children:
                return False
            current = current.children[sym]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
