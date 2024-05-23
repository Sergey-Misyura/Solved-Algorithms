"""
131. Palindrome Partitioning
(Medium complexity)

Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def dfs(s, path, ans):  # dfs
            if not s:  # если нет строки - добавляем путь в ответ
                ans.append(path[:])
                return
            for i in range(1, len(s)+1):  # проходим по строке
                if s[:i] == s[i-1::-1]:  # если от начала до i палиндром
                    path.append(s[:i])  # добавляем палиндром в путь
                    dfs(s[i:], path, ans)  # вызываем dfs c оставшейся частью строки
                    path.pop()  # убираем палиндром из пути

        ans = []  # ответ
        dfs(s, [], ans)  # запускаем dfs
        # ответ
        return ans