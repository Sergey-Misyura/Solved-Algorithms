"""
451. Sort Characters By Frequency
(Medium complexity)

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        ans = []
        for key, value in sorted(count.items(), key=lambda x: -x[1]):
            ans.append(key * value)

        return ''.join(ans)