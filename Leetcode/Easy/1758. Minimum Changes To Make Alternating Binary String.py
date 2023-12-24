"""
1758. Minimum Changes To Make Alternating Binary String
(Easy complexity)

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""


class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        cur_need = 0
        for i in range(len(s)):
            ans += cur_need == int(s[i])
            cur_need = 1 - cur_need

        return min(ans, len(s) - ans)