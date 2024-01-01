"""
455. Assign Cookies
(Easy complexity)

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        g.sort(reverse=True)
        s.sort(reverse=True)

        total = 0
        cur_g = 0
        for num in s:

            while cur_g < len(g) and g[cur_g] > num:
                cur_g += 1
            if cur_g < len(g):
                cur_g += 1
                total += 1

        return total


