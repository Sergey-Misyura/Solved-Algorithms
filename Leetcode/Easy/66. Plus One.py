"""
66. Plus One
(Easy complexity)
You are given a large integer represented as an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 1
        idx = len(digits)-1

        while (temp > 0) and idx != -1:
            temp, digits[idx] = divmod(digits[idx]+temp, 10)
            idx-=1
        if idx==-1 and temp !=0:
            digits.insert(0, temp)
        
        return digits