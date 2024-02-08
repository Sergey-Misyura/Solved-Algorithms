"""
1768. Merge Strings Alternately
(Easy complexity)

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)

        ans = [0] * (2 * min(n, m))
        cur_n, cur_m = 0, 0
        cur_ans = 0
        while cur_n < n and cur_m < m:
            ans[cur_ans] = word1[cur_n]
            cur_ans += 1
            ans[cur_ans] = word2[cur_m]
            cur_ans += 1
            cur_n += 1;
            cur_m += 1

        ans = ''.join(ans)

        if n == m:
            return ans
        elif n > m:
            return ans + word1[cur_n:]
        else:
            return ans + word2[cur_m:]