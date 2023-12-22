"""
1422. Maximum Score After Splitting a String
(Easy complexity)

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
"""

class Solution:
    def maxScore(self, s: str) -> int:
        ans = total = s.count("1")
        for i in range(1, len(s)-1):
            if s[i] == '0':
                total +=1
            else:
                total -=1
            ans = max(ans, total)

        return ans-1 if s[0] == '1' else ans+1