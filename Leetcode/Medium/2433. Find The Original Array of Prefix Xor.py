"""
2433. Find The Original Array of Prefix Xor
(Medium complexity)

You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.
"""

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        for i in range (len(pref)-1, 0, -1):
            pref[i] ^= pref[i-1]
        return pref