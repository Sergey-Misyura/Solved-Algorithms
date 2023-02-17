"""
14. Longest Common Prefix
(Easy complexity)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos = 1
        pref = ""
        total = ""
        prefix_is = True
        minlen = len(strs[0])

        while prefix_is and (pos<=minlen):
            for word in strs:
                total +=word[:pos]
            if total==word[:pos]*len(strs):
                pref = word[:pos]
                pos +=1
                total = ""
            else: 
                prefix_is = False

        return pref