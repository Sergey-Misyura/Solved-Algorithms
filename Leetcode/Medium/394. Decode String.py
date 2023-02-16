"""
394. Decode String
(Medium complexity)

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10**5.
"""
class Solution:
    def decodeString(self, s: str) -> str:

        stack, repeats, cur, prev = [], 0, '', ''

        for sym in s:
            if sym.isdigit(): 
                repeats=repeats*10+int(sym)

            elif sym.isalpha():
                cur +=sym
                    
            elif sym =='[':
                stack.append(cur)
                stack.append(repeats)
                cur, repeats = '', 0 

            elif sym ==']':
                repeats, prev = stack.pop(), stack.pop()
                cur = prev + repeats*cur
                repeats=0
            
        return cur