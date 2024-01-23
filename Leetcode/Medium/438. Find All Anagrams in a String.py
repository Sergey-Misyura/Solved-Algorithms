"""
438. Find All Anagrams in a String
(Medium complexity)

Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []

        s_count, p_count = [0] * 26, [0] * 26
        ans = []

        for i in range(len_p):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        if s_count == p_count:
            ans.append(0)

        for i in range(len_p, len_s):
            s_count[ord(s[i]) - 97] += 1
            s_count[ord(s[i - len_p]) - 97] -= 1
            if s_count == p_count:
                ans.append(i - len_p + 1)

        return ans