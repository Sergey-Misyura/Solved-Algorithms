"""
24. Swap Nodes in Pairs
(Medium complexity)

ou are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements."""


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        dp = [set()]
        for seq in arr:
            set_seq = set(seq)
            if len(set_seq) == len(seq):
                for prev in dp[:]:
                    if not prev & set_seq:
                        dp.append(set_seq | prev)

        return max(len(set_seq) for set_seq in dp)
