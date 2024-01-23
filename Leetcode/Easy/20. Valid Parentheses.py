"""
20. Valid Parentheses
(Easy complexity)

Given a string s containing just the characters '(', ')', '{' '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'[':']', '(': ')', '{': '}',
                    ']':'[', ')': '(', '}': '{'}
        opening, ending = set(['[', '(', '{']), set([']', ')', '}'])
        stack = []

        for sym in s:
            if sym in opening:
                stack.append(sym)

            if sym in ending:
                if not stack:
                    return False
                if stack[-1] == brackets[sym]:
                    stack.pop()
                else:
                    return False


        return not stack 