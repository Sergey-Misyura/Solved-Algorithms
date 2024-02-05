"""
387. First Unique Character in a String
(Easy complexity)

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq_set = set()
        not_uniq_set = set()
        indexes = [float('inf')] * 26
        for i in range(len(s)):
            if s[i] not in not_uniq_set:
                if s[i] not in uniq_set:
                    uniq_set.add(s[i])
                    indexes[ord(s[i]) - 97] = i
                else:
                    uniq_set.remove(s[i])
                    not_uniq_set.add(s[i])
                    indexes[ord(s[i]) - 97] = float('inf')

        first_idx = min(indexes)
        return first_idx if first_idx != float('inf') else -1