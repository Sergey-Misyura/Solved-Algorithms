"""
3. Longest Substring Without Repeating Characters
(Medium complexity)

Given a string s, find the length of the longest
substring
 without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        counter = defaultdict(int)
        max_len = first = second = 0

        while second < len(s):

            counter[s[second]] += 1

            while counter[s[second]] == 2:
                counter[s[first]] -= 1
                first += 1

            max_len = len(s[first:second]) + 1 if len(s[first:second]) + 1 > max_len else max_len
            second += 1

        return max_len

